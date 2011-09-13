#/bin/python

import bottle
from bottle import template, request
from pprint import pprint
from models import *
from demo_locations import route
from sqlalchemy.orm.exc import NoResultFound

import datetime
import json
import urllib

from bottle import request
from hack.helper import parse_accel
from pprint import pprint

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

PLACES_KEY = 'AIzaSyCvfId0lM9v_F2igUi4AIRbFJHr8IlMFAY'
PLACES_API = 'https://maps.googleapis.com/maps/api/place/search/json'

BACK_END = bottle.Bottle()

class EchonestMagicError(Exception):
  pass

class SearchError(Exception):
   pass

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

  place_type = coord_to_place_type()
  

@BACK_END.route( '/recommend' )
def recommend():
  category = get_user_category(request.GET)

  # TODO: get parameters for echonest based on category
  args = {\
      'api_key' : ECHONEST_KEY,\

      # limit songs to those found in 7digital catalog
      'bucket'  : 'id:7digital-US',\
      'limit'   : 'true',\

      # TODO: our own magic parameters
      'artist'  : 'Calvin Harris',\
  }

  url = ECHONEST_API + '?' + urllib.urlencode(args) + '&bucket=tracks'
  result = json.load(urllib.urlopen(url))

  echonest_status = result['response']['status']
  if echonest_status['code'] != 0:
    print 'Error querying Echonest:', echonest_status['message']
    raise EchonestMagicError

  #pprint(result)
  return json.dumps( result['response']['songs'] )

@BACK_END.route('/places_magic', method='GET')
def places_magic():
  latitude = request.GET.get('latitude', '').strip()
  longitude = request.GET.get('longitude', '').strip()

  r = ''

  for coords in route:
    r += ('%s,%s' % (coords.lat, coords.lng)) + ': '
    r += coordToPlaceType(coords) + '<br/>'

  return r

def coordToPlaceType(coords):  
  places_types = [
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

  args = {\
        'location' : '%s,%s' % (coords.lat, coords.lng),\
        'radius'   : 10,\
        'sensor'   : 'true',\
        'key'      : PLACES_KEY,\
        'types'    : '|'.join(places_types)
  }

  url = PLACES_API + '?' + urllib.urlencode(args)
  result = json.load(urllib.urlopen(url))

  if 'Error' in result:
      # An error occurred; raise an exception
      raise SearchError, result['Error']

  for t in result['results'][0]['types']:
      if t in places_types:
        return t

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
