import bottle
from bottle import template, static_file
from settings import STATIC_PATH

FRONT_END = bottle.Bottle()

@FRONT_END.route( '/index' )
def front_end_index():
    return template( 'index' )