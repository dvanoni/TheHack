#/bin/python

import bottle
from bottle import template, request
from pprint import pprint

import json
import urllib

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

PLACES_KEY = 'AIzaSyCvfId0lM9v_F2igUi4AIRbFJHr8IlMFAY'
PLACES_API = 'https://maps.googleapis.com/maps/api/place/search/json'

BACK_END = bottle.Bottle()

class EchonestMagicError(Exception):
  pass

class SearchError(Exception):
   pass

@BACK_END.route('/echonest_magic', method='GET')
def echonest_magic():
  # TODO: grab phone data
  x_coordinate = request.GET.get('x_coordinate', '').strip()
  y_coordinate = request.GET.get('y_coordinate', '').strip()
  z_coordinate = request.GET.get('z_coordinate', '').strip()
  timestamp = request.GET.get('timestamp', '').strip()
  gps_location = request.GET.get('gps_location', '').strip()

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

  pprint(result)
  songs = result['response']['songs']

  return template('song_dump', songs=songs)

@BACK_END.route('/places_magic', method='GET')
def places_magic():
  latitude = request.GET.get('latitude', '').strip()
  longitude = request.GET.get('longitude', '').strip()

  #TODO: the moma
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

  return place['types']
