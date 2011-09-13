#/bin/python

import bottle
import datetime
import json
import urllib

from bottle import request
from demo_locations import route
from hack.helper import parse_accel, analyze_accel
from models import *
from pprint import pprint
from sqlalchemy.orm.exc import NoResultFound

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

PLACES_KEY = 'AIzaSyCvfId0lM9v_F2igUi4AIRbFJHr8IlMFAY'
PLACES_API = 'https://maps.googleapis.com/maps/api/place/search/json'

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

#TODO: add weather
USER_CATEGORIES = {
  'studying'     : {
      'max_tempo' : '200',
      'max_danceability' : '.5',
      'max_energy' : '.5'
    },
  'running'      : {
      'min_tempo' : '300',
      'min_danceability' : '.5',
      'min_energy' : '.5'
    },
  'commuting'    : {
      'min_tempo' : '300',
      'min_danceability' : '.4',
      'min_energy' : '.35'
    },
  'walking'      : {
      'min_tempo' : '200',
      'min_danceability' : '.35',
      'min_energy' : '.3'
    },
  'waking_up'    : {
      'max_tempo' : '200',
      'max_energy' : '.5',
      'mood' : 'happy'
    },
  'winding_down' : {
      'max_tempo' : '300',
      'max_energy' : '.7',
      'mood' : 'happy'
    },
  'pre_party'    : {
      'min_danceability' : '.7',
      'min_energy' : '.5',
      'mood' : 'happy'
    }
}

class EchonestMagicError(Exception):
  pass

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
  user_state = analyze_accel( ax, ay, az )
  
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

  # TODO: use USER_CATEGORIES
  args = {
      'api_key' : ECHONEST_KEY,

      # limit songs to those found in 7digital catalog
      'bucket'  : 'id:7digital-US',
      'limit'   : 'true'
  }

  args.update(USER_CATEGORIES['waking_up'])

  url = ECHONEST_API + '?' + urllib.urlencode(args) + '&bucket=tracks'
  result = json.load(urllib.urlopen(url))

  echonest_status = result['response']['status']
  if echonest_status['code'] != 0:
    print 'Error querying Echonest:', echonest_status['message']
    raise EchonestMagicError

  #pprint(result)
  #return json.dumps( result['response']['songs'] )

  track_data = []
  print 'found %d songs!' % len(result['response']['songs'])

  for s in result['response']['songs']:
    if 'title' not in s:
      continue

    artist = ''
    if 'artist_name' in s:
      artist = s['artist_name']
    
    preview_url = ''
    album_img = ''
    if 'tracks' in s:
      preview_url = s['tracks'][0]['preview_url']
      album_img = s['tracks'][0]['release_image']

    track_data.append({
        'name'        : s['title'],
        'artist'      : artist,
        'preview_url' : preview_url,
        'album_img'   : album_img
    })

  return json.dumps(track_data)

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
