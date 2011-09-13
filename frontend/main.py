#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Andrew Huynh on 2011-09-13.
Copyright (c) 2011 athlabs. All rights reserved.
"""
import bottle
from bottle import run, template, static_file
from settings import STATIC_PATH

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
    return template( 'index' )
    
if __name__ == '__main__':
    run( MAIN, host='localhost', port=8080, reloader=True )