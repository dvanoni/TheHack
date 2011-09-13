#/bin/python

import bottle
from bottle import template, request
from pprint import pprint
from models import *
from demo_locations import route
from sqlalchemy.orm.exc import NoResultFound

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

  r = ''

  for coords in route:

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

    r += ('%s,%s' % (coords.lat, coords.lng)) + '<br/>'
    r += ', '.join(result['results'][0]['types']) + '<br/>'

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