import bottle
from bottle import template, static_file
from PIL import Image
from settings import STATIC_PATH

FRONT_END = bottle.Bottle()

@FRONT_END.route( '/index' )
def front_end_index():
    return template( 'index' )

@FRONT_END.route( '/dominant_color' )
def dominant_color():
    img = request.GET.get( '')
    color = img.resize( (1,1), Image.ANTIALIAS).getpixel((0,0))  