import bottle

from bottle import template, static_file, request
from PIL import Image
from settings import STATIC_PATH

FRONT_END = bottle.Bottle()

@FRONT_END.route( '/index' )
def front_end_index():
	login = True
	s = bottle.request.environ.get('beaker.session')
	username = s.get('username')

	if username:
		login = False

	return template('index', login=login, username=username)
	
@FRONT_END.route( '/dominant_color' )
def dominant_color():
    img = request.GET.get( '')
    color = img.resize( (1,1), Image.ANTIALIAS).getpixel((0,0))  

