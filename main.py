import bottle

from bottle import redirect, run, static_file

from backend.server import BACK_END

from frontend.settings import STATIC_PATH
from frontend.main import FRONT_END

# Set debug mode and create the main bottle application
bottle.debug( True )
MAIN = bottle.Bottle()

@MAIN.route( '/static/:path#.+#')
def server_static( path ):
    '''
    Return static files situated at STATIC_PATH
    '''
    return static_file( path, root=STATIC_PATH )

@MAIN.route( '/' )
def index():
    return redirect( '/front_end/index' )

# Attach API functions
MAIN.mount( FRONT_END, '/front_end' )
MAIN.mount( BACK_END, '/api' )
if __name__ == '__main__':    
    run( MAIN, host='localhost', port=8080, reloader=True )