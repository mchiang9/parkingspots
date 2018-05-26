from django.db import models
# Create your models here.

class Spot(models.Model):
	identity = models.IntegerField()
	lat = models.DecimalField(max_digits = 7, decimal_places=2)
	lon = models.DecimalField(max_digits = 7, decimal_places=2)
	reserved = models.BooleanField()

	def __int__(self):
		return self.identity

	def distance(self,x1,x2,y1,y2):
		x1 = float(x1)
		x2 = float(x2)
		y1 = float(y1)
		y2 = float(y2)
		return ((x1-x2)**2 + (y1-y2)**2)**.5

	def inRange(self,radius,trueDist):
		return ((trueDist <= radius) == True)