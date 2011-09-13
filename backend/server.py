#/bin/python

import bottle
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

@BACK_END.route( '/recommend' )
def recommend():
  # Grab phone data
  accel_data  = request.GET.get( 'accelerometer' )
  timestamp   = request.GET.get( 'timestamp' )
  latitude    = request.GET.get( 'latitude' )
  longitude   = request.GET.get( 'longitude' )
  
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
    latitude  = 40.77905519999999
    longitude = -73.96283459999999
  else:
    latitude  = float( latitude )
    longitude = float( longitude )
  
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

  #TODO: the moma
  if len( latitude ) == 0 or len( longitude ) == 0:
    latitude = '40.77905519999999'
    longitude = '-73.96283459999999'
    
  args = {\
      'location' : '%s,%s' % (latitude, longitude),\
      'radius'   : 10,\
      'sensor'   : 'true',\
      'key'      : PLACES_KEY
  }

  url = PLACES_API + '?' + urllib.urlencode(args)
  result = json.load(urllib.urlopen(url))

  if 'Error' in result:
    # An error occurred; raise an exception
    raise SearchError, result['Error']

  # grab the categories of the first place
  place = result['results'][0]

  return json.dumps( place )
