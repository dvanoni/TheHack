import bottle

from bottle import template, static_file, request
from PIL import Image
from settings import STATIC_PATH

import json
import urllib

FRONT_END = bottle.Bottle()

@FRONT_END.route( '/index' )
def front_end_index():
	login = True
	s = bottle.request.environ.get('beaker.session')

	if s:
		username = s.get('username')
		profile_id = s.get('profile_id')
		access_token = s.get('access_token')
		fb_image = "https://graph.facebook.com/me/picture?access_token=%s" % access_token
		fb_music = "https://graph.facebook.com/me/music?access_token=%s" % access_token
		music = json.load(urllib.urlopen(fb_music))

	else:
		username = None
		fb_image = None

	if username:
		login = False

	return template('index', login=login, username=username, fb_image=fb_image, my_music=music)
	
@FRONT_END.route( '/dominant_color' )
def dominant_color():
    img = request.GET.get( '')
    color = img.resize( (1,1), Image.ANTIALIAS).getpixel((0,0))  

