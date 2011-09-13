# Models.py
# Maps python classes to tables in the database

from alchemy import *

class AppData(Base):
	__tablename__ = 'appdata'

	app_name = Column(String, primary_key=True)
	version_number = Column(String)
	description = Column(String)

	def __init__(self, app_name, version_number, descrption):
		self.app_name = app_name
		self.version_number = version_number
		self.description = description

	def __repr__(self):
		return "%s Version %s - %s" % (self.app_name, self.version_number, self.description)

class Coordinate(Base):
	__tablename__ = 'coordinates'

	id = Column(Integer, primary_key=True)
	lat = Column(Float)
	lng = Column(Float)

	def __init__(self, lat, lng):
		self.lat = lat
		self.lng = lng

	def __repr__(self):
		return "Coord <%s,%s>" % (self.lat, self.lng)
