from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from . models import Spot

 
@api_view(['GET', ])
def available(request,lat,lon,radius):
	try: 
		lat = float(lat)
		lon = float(lon)
		radius = float(radius)
	# Never reach ValueError since regex will take care of invalid requests
	except ValueError:
		raise ValidationError("Unexpected parameters - please make sure lat, lon, and radius are valid floating point values")

	inRangeSpots = []
	for parkSpots in Spot.objects.all():
		if parkSpots.inRange(radius, 
			parkSpots.distance(parkSpots.lat,lat,parkSpots.lon,lon)):
			if(parkSpots.reserved == False):
				inRangeSpots.append({"id": parkSpots.identity, "lat": parkSpots.lat, "lon": parkSpots.lon})
	return JsonResponse(inRangeSpots, safe = False)

@api_view(['POST', ])
def reserve(request, idx):
	parkSpot = Spot.objects.get(identity=idx)
	if not parkSpot:
		raise ValidationError("Could not find spot with id: " + str(idx))
	parkSpot.reserved = True
	parkSpot.save()
	return JsonResponse({"reserved": "true"})


@api_view(['GET', ])
def is_reserved(request, idx):
	parkSpot = Spot.objects.get(identity=idx)
	if not parkSpot:
		raise ValidationError("Could not find spot with id: " + str(idx))
	return JsonResponse({"reserved": parkSpot.reserved})













