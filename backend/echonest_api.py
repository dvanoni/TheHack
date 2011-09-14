#/bin/python

import json
from pprint import pprint
import sys
import urllib

ECHONEST_KEY = 'YBBLFZVQBRPQF1VKS'
ECHONEST_API = 'http://developer.echonest.com/api/v4/song/search'

USER_CATEGORIES = {
  'studying'     : {
      'sort' : 'song_hotttnesss-desc',
      'max_danceability' : '.2',
      'max_energy' : '.2',
      'max_loudness' : '20'
    },
  'running'      : {
      'sort' : 'song_hotttnesss-desc',
      'min_tempo' : '240',
      'min_danceability' : '.6',
      'min_energy' : '.6'
    },
  'commuting'    : {
      'song_min_hotttnesss' : '.75',
      'min_danceability' : '.5',
      'min_energy' : '.5'
    },
  'walking'      : {    
      'sort' : 'song_hotttnesss-desc',
      'min_tempo' : '200',
      'min_danceability' : '.35',
      'min_energy' : '.5'
    },
  'waking_up'    : {
      'sort' : 'song_hotttnesss-desc',
      'max_energy' : '.4',
    },
  'winding_down' : {
      'max_tempo' : '80',
      'sort' : 'song_hotttnesss-desc'
    },
  'pre_party'    : {
      'song_min_hotttnesss' : '.85',
      'artist_start_year_after' : '2000'
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
