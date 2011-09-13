import bottle
from bottle import run

bottle.debug( True )
MAIN = bottle.Bottle()

@MAIN.route( '/' )
def index():
    return 'Hello World'
    
if __name__ == '__main__':
    run( MAIN, host='localhost', port=8080, reloader=True )
