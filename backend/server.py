#/bin/python

import bottle
from bottle import template, request, redirect, response
from pprint import pprint
from models import *
from demo_locations import route
from sqlalchemy.orm.exc import NoResultFound
from beaker.middleware import SessionMiddleware

import datetime
import json
import urllib
import cgi
import base64
import Cookie
import email.utils

from bottle import request
from pprint import pprint

from hack.helper import *

import echonest_api as echonest
import places_api as places

from echonest_api import UserCategory


FACEBOOK_APP_ID = '170844926329169'
FACEBOOK_SECRET = '04e620adbd4f35209b04dda6269bf408'
REDIRECT_URL    = 'http://thehack.dvanoni.com/api/facebook'

BACK_END = bottle.Bottle()

ROUTE_COUNTER = 0

def parse_user_attributes(get_request):
  global ROUTE_COUNTER
  # Grab phone data
  accel_data  = get_request.get('accelerometer')
  timestamp   = get_request.get('timestamp')

  # default to route
  latitude    = route[ROUTE_COUNTER].lat
  longitude   = route[ROUTE_COUNTER].lng
  if (ROUTE_COUNTER >= len(route) - 1): 
    ROUTE_COUNTER = 0
  else: 
    ROUTE_COUNTER+=1

  # parse phone data
  place_type = places.coord_to_place_type(latitude, longitude)
  user_state = UserState.SITTING
  ax, ay, az = parse_accel(accel_data)
  if ax is not None and ay is not None and az is not None:
    user_state = analyze_accel(ax, ay, az)
  day_state = analyze_timestamp(timestamp)

  return (place_type, day_state, user_state)

def get_user_category(place_type, day_state, user_state):

  # special cases
  if place_type is 'park'\
      and user_state is UserState.SITTING\
      or user_state is UserState.WALKING:
    return UserCategory.STUDYING

  if place_type is 'park' and user_state is UserState.RUNNING:
    return UserCategory.RUNNING
  if place_type in places.WORKOUT:
    category = UserCategory.RUNNING
  elif place_type in places.LOWKEY:
    category = UserCategory.WALKING
  elif place_type in places.SOCIAL:
    category = UserCategory.PRE_PARTY
  elif place_type in places.TRAVEL:
    category = UserCategory.COMMUTING
  elif place_type in places.STUDY:
    category = UserCategory.STUDYING
  else:
    print 'Using default category'
    category = UserCategory.PRE_PARTY  # the default

  return category

@BACK_END.route( '/similar', method='GET' )
def similar():
  moods = {'happy','upbeat','inspiring'}
  return json.dumps(echonest.getSimilarMood(moods))
  
@BACK_END.route( '/recommend' )
def recommend():
  debug = False
  if request.GET.get('debug') is '1':
    print 'Running debug...'
    debug = True

  (place_state, user_state, day_state) = parse_user_attributes(request.GET)
  category = get_user_category(place_state, user_state, day_state)

  if debug:
    category = request.GET.get('c', '').strip()

  #TODO: hacked to work on thehack
  category = UserCategory.PRE_PARTY
  track_data = echonest.getCategory(category)

  if debug:
    return template('song_dump', tracks=track_data)
  else:
    return json.dumps(track_data)

@BACK_END.route('/places_magic', method='GET')
def places_magic():
  latitude = request.GET.get('latitude', '').strip()
  longitude = request.GET.get('longitude', '').strip()

  r = ''

  for coords in route:
    r += ('%s,%s' % (coords.lat, coords.lng)) + ': '
    r += places.coord_to_place_type(coords.lat, coords.lng) + '<br/>'

  return r

@BACK_END.route('/coords', method='GET')
def coords():
  session = Session();
  lat = request.GET.get('lat', '').strip()
  lng = request.GET.get('lng', '').strip()

  try:
    location = session.query(Coordinate).filter(Coordinate.lat==lat).filter(Coordinate.lng==lng).one()
    return str(location)
  except NoResultFound, e:
    return "Location was not found in our database"

@BACK_END.route('/facebook', method='GET')
def facebook_login():
  session = Session()
  code = request.GET.get('code')
  if code:
    fb_url = "https://graph.facebook.com/oauth/access_token?client_id="+FACEBOOK_APP_ID+"&redirect_uri="+REDIRECT_URL+"&client_secret="+FACEBOOK_SECRET+"&code="+code
    fb_response = cgi.parse_qs(urllib.urlopen(fb_url).read())
    access_token = fb_response["access_token"][-1]
    profile = json.load(urllib.urlopen("https://graph.facebook.com/me?" + urllib.urlencode(dict(access_token=access_token))))
    profile_id = str(profile["id"])
    user = User(name=profile["name"], profile_id=profile_id, access_token=access_token)
    session.merge(user)
    session.commit()
    s = bottle.request.environ.get('beaker.session')
    s['username'] = profile["name"]
    s['profile_id'] = profile_id
    s['access_token'] = access_token
    s.save()
  redirect("/")

@BACK_END.route('/logout', method='GET')
def logout():
  s = bottle.request.environ.get('beaker.session')
  s.delete()
  redirect("/")
