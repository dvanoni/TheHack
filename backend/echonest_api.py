#/bin/python

import json
from pprint import pprint
import sys
import urllib

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

USER_CATEGORIES = {
  'studying'     : {
      'max_tempo' : '100',
      'max_danceability' : '.5',
      'max_energy' : '.5'
    },
  'running'      : {
      'min_tempo' : '200',
      'min_danceability' : '.5',
      'min_energy' : '.5'
    },
  'commuting'    : {
      'min_tempo' : '200',
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
      'min_danceability' : '.3',
    }
}

class EchonestMagicError(Exception):
  pass

def search(category):
  print 'echonest search for:', category

  args = {
      'api_key' : ECHONEST_KEY,

      # limit songs to those found in 7digital catalog
      'bucket'  : 'id:7digital-US',
      'limit'   : 'true'
  }

  args.update(USER_CATEGORIES[category])

  url = ECHONEST_API + '?' + urllib.urlencode(args) + '&bucket=tracks'
  result = json.load(urllib.urlopen(url))

  echonest_status = result['response']['status']
  if echonest_status['code'] != 0:
    print 'UGHHH echonest error!', echonest_status['message']
    return

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
      if s['tracks'][0]:
        if s['tracks'][0]['preview_url']:
          preview_url = s['tracks'][0]['preview_url']
        if s['tracks'][0]['release_image']:
          album_img = s['tracks'][0]['release_image']

    track_data.append({
        'name'        : s['title'],
        'artist'      : artist,
        'preview_url' : preview_url,
        'album_img'   : album_img
    })

  return track_data
