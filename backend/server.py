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
from hack.helper import parse_accel
from pprint import pprint
import echonest_api as echonest

PLACES_KEY = 'AIzaSyCvfId0lM9v_F2igUi4AIRbFJHr8IlMFAY'
PLACES_API = 'https://maps.googleapis.com/maps/api/place/search/json'

FACEBOOK_APP_ID = '170844926329169'
FACEBOOK_SECRET = '04e620adbd4f35209b04dda6269bf408'
REDIRECT_URL    = 'http://thehack.dvanoni.com/api/facebook'

BACK_END = bottle.Bottle()

PLACE_TYPES = [
  # WORKOUT
  'gym',
  'health',
  # LOW KEY
  'museum',
  'park',
  'aquarium',
  'art_gallery',
  'cafe',
  'spa',
  # SOCIAL
  'bar',
  'night_club',
  # TRAVEL
  'subway_station',
  'taxi_stand',
  'train_station',
  # STUDY
  'book_store',
  'library',
  'university',
  'school'
]

class SearchError(Exception):
   pass

def coord_to_place_type(lat, lng):  
  args = {
        'location' : '%s,%s' % (lat, lng),
        'radius'   : 10,
        'sensor'   : 'true',
        'key'      : PLACES_KEY,
        'types'    : '|'.join(PLACE_TYPES)
  }

  url = PLACES_API + '?' + urllib.urlencode(args)
  result = json.load(urllib.urlopen(url))

  if 'Error' in result:
    # An error occurred; raise an exception
    raise SearchError, result['Error']
      
  if result[ 'status' ] == 'ZERO_RESULTS':
    raise SearchError, 'Zero results'
  
  for t in result['results'][0]['types']:
    if t in PLACE_TYPES:
      return t


def get_user_category(get_request):
  # Grab phone data
  accel_data  = get_request.get( 'accelerometer' )
  timestamp   = get_request.get( 'timestamp' )
  latitude    = get_request.get( 'latitude' )
  longitude   = get_request.get( 'longitude' )

  # parse phone data
  ax, ay, az = parse_accel( accel_data )
  
  # Convert timestamp into a python datetime object
  try:
    timestamp = datetime.datetime.fromtimestamp( float( timestamp ) )
  except Exception:
    # use the server time if we can't parse the sucker
    timestamp = datetime.datetime.now()
  
  # Convert lat/lng into floats
  if latitude is None or longitude is None:
    # If no lat/lng is specified, default to the MOMA
    latitude  = 40.77905519999999
    longitude = -73.96283459999999
  else:
    latitude  = float( latitude )
    longitude = float( longitude )

  place_type = coord_to_place_type(latitude, longitude)
  
@BACK_END.route( '/recommend' )
def recommend():
  category = get_user_category(request.GET)

  # TODO: for debugging
  category = request.GET.get('c', '').strip()

  track_data = echonest.search(category)

  #return json.dumps(track_data)

  # for debugging
  return template('song_dump', tracks=track_data)

@BACK_END.route('/places_magic', method='GET')
def places_magic():
  latitude = request.GET.get('latitude', '').strip()
  longitude = request.GET.get('longitude', '').strip()

  r = ''

  for coords in route:
    r += ('%s,%s' % (coords.lat, coords.lng)) + ': '
    r += coord_to_place_type(coords.lat, coords.lng) + '<br/>'

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
    s = bottle.request.environ.get('beaker.session')
    s['username'] = profile["name"]
    s['profile_id'] = profile_id
    s.save()
  redirect("/")

