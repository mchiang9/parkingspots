from django.test import TestCase

# Create your tests here.

from . models import Spot
from . import views

class SpotTests(TestCase):

	def unreserved_spot_in_same_spot(self):
		# Test to when Reserve = False
		# Lat Lon are same coordinates as location
		same_spot = Spot(identity = 1, lat = 37.50,lon = -122.40,reserved = False)

