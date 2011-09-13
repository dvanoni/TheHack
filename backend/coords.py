#/bin/python

import bottle
from bottle import template, request
from pprint import pprint
from models import *

import json
import urllib


BACK_END = bottle.Bottle()

class EchonestMagicError(Exception):
  pass

@BACK_END.route('/coords', method='GET')
def coords():
  lat = request.GET.get('lat', '').strip()
  lng = request.GET.get('lng', '').strip()

  try:
    location = session.query(Coordinate).filter(Coordinate.lat==lat).filter(Coordinate.lng==lng);
    print "Found location!"
  except NoResultFound, e:
    print "Location was not found in our database"