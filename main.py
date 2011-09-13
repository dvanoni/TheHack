import bottle
from bottle import run
from frontend.main import FRONT_END

MAIN = bottle.Bottle()

@MAIN.route( '/' )
def index():
    return 'Hello World'
    
# Attach API functions
MAIN.mount( FRONT_END, '/front_end' )

if __name__ == '__main__':
    run( MAIN, host='localhost', port=8080, reloader=True )
