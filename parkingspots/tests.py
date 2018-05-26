from django.test import TestCase
from django.test import Client

# Create your tests here.

from . models import Spot
from . import views

class SpotTests(TestCase):

	# def test_unreserved_spot_in_same_spot(self):
	# 	# Test to when Reserve = False
	# 	# Lat Lon are same coordinates as location and identity is same
	# 	# Tests to ensure functions are consistent
	# 	lat = 37.50
	# 	lon = -122.40
	# 	radius = 0.0
	# 	same_spot = Spot(identity = 0, lat = lat,lon = lon,reserved = False)
	# 	same_spot2 = Spot(identity = 0, lat = lat,lon = lon,reserved = False)
	# 	self.assertEquals(views.available(same_spot,lat,lon,radius),views.available(same_spot2,lat,lon,radius))

	# cust_lat = 39.50
	# cust_lon = -120.40
	# radius = 10.0

	# lat1 = 33.50
	# lon1 = -124.40
	# spot1 = Spot(identity = 1, lat = lat1,lon = lon1,reserved = False)

	def test_unreserved_spot_in_range(self):
		# Test to when Reserve = False
		# Lat Lon are in range of location
		cust_lat = 39.50
		cust_lon = -120.40
		radius = 10.0

		lat1 = 33.50
		lon1 = -124.40
		spot1 = Spot(identity = 1, lat = lat1,lon = lon1,reserved = False)
		self.assertIs(spot1.inRange(radius,spot1.distance(cust_lat,spot1.lat,cust_lon,spot1.lon)),True)

	def test_unreserved_spot_out_of_radius_range(self):
		# Test when Reserve = False
		# Lat Lon are not in radius range of location
		cust_lat = 39.50
		cust_lon = -120.40
		radius = 5.0

		lat1 = 33.50
		lon1 = -124.40
		spot1 = Spot(identity = 1, lat = lat1,lon = lon1,reserved = False)
		self.assertIs(spot1.inRange(radius,spot1.distance(cust_lat,spot1.lat,cust_lon,spot1.lon)),False)


	def test_unreserved_spot_out_of_range(self):
		# Test when Reserve = False
		# Lat Lon are not in range of 
		cust_lat = 39.50
		cust_lon = -120.40
		radius = 5.0

		lat2 = 0
		lon2 = 0
		spot2 = Spot(identity = 2, lat = lat2,lon = lon2,reserved = False)
		self.assertIs(spot2.inRange(radius,spot2.distance(cust_lat,spot2.lat,cust_lon,spot2.lon)),False)

	def test_reserved_spot_in_range(self):
		# Test to see if the outputs between spot1 and spot3 are the same even though the only difference
		# is the reserved boolean
		cust_lat = 39.50
		cust_lon = -120.40
		radius = 10.0

		lat1 = 33.50
		lon1 = -124.40
		spot3 = Spot(identity = 1, lat = lat1,lon = lon1,reserved = True)
		trueDist = spot3.distance(cust_lat,spot3.lat,cust_lon,spot3.lon)
		# print(spot3.reserved)
		self.assertIs(spot3.spotAvailable(radius,trueDist),False)

	def test_reserved_spot_out_of_range(self):
		cust_lat = 39.50
		cust_lon = -120.40
		radius = 0

		lat1 = 33.50
		lon1 = -124.40
		spot3 = Spot(identity = 1, lat = lat1,lon = lon1,reserved = True)
		# print(spot3.reserved)
		# print(spot3.InRange(spt3spot3.isNotReserved())
		trueDist = spot3.distance(cust_lat,spot3.lat,cust_lon,spot3.lon)
		self.assertIs(spot3.spotAvailable(radius,trueDist),False)

	# def test_get_statement(self):
	# 	response = Client.get('/api/v1/parkingspots/available/37.5/-122.5/10.0')
	# 	response.content

