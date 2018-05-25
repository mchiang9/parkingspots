from django.db import models
import math
# Create your models here.

class spots(models.Model):
	identity = models.IntegerField()
	lat = models.DecimalField(max_digits = 7, decimal_places=2)
	lon = models.DecimalField(max_digits = 7, decimal_places=2)
	reserved = models.BooleanField()

	def __int__(self):
		return self.identity

	def haversine(self,x1,x2,y1,y2):
		lat1 = math.radians(x1)
		lat2 = math.radians(x2)
		lon1 = math.radians(y1)
		lon2 = math.radians(y2)
		delt_lat = (lat2-lat1)
		delt_lon = (lon2-lon1)
		# Haversine Formula
		a = ((math.sin(delt_lat))**2)+ math.cos(lat1)*math.cos(lat2)+((math.sin(delt_lon))**2)
		c = (2 * math.atan2(a**0.5, math.fabs((1-a))**0.5))
		# Earth's Radius in km
		R = 6371
		return R*c

	def inRange(self,radius,trueDist):
		return ((trueDist <= radius) == True)