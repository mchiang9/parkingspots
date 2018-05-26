from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Spot
from . serializers import spotsSerializer
from django.core import serializers
import math
 



# @api_view(['GET', ])
# def available(request,lat,lon,radius):
# 	# cust_Lat = request.GET.get('lat',0)
# 	# cust_Lon = request.GET.get('lon',0)
# 	# cust_Radius = request.GET.get('radius',0)
# 	try: 
# 		lat = float(lat)
# 		lon = float(lon)
# 		radius = float(radius)
# 		print("POOOP")
# 		print(lat, lon, radius)
# 	except ValueError:
# 	    # should not happen if regex is correct 
# 	    # perhaps replace print statement with a suitable Response to client 
# 	     print("Request parameters are invalid")
# 	inRangeIDs = []
# 	for parkSpots in Spot.objects.all():
# 		if (parkSpots.inRange(radius, 
# 		parkSpots.haversine(parkSpots.lat,lat
# 		,parkSpots.lon,lon)) == True):

# 			inRangeIDs.append(parkSpots.identity)
# 	print(inRangeIDs)
# 	spots1 = Spot.objects.filter(reserved = False 
# 			, identity__in = inRangeIDs
# 			 )

# 	serializer = spotsSerializer(spots1, many= True)
# 	return Response(serializer.data@api_view(['GET', ])
@api_view(['GET', ])
def available(request,lat,lon,radius):
	# cust_Lat = request.GET.get('lat',0)
	# cust_Lon = request.GET.get('lon',0)
	# cust_Radius = request.GET.get('radius',0)
	try: 
		lat = float(lat)
		lon = float(lon)
		radius = float(radius)
		print("POOOP")
		print(lat, lon, radius)
	except ValueError:
	    # should not happen if regex is correct 
	    # perhaps replace print statement with a suitable Response to client 
	     print("Request parameters are invalid")
	inRangeSpots = []
	for parkSpots in Spot.objects.all():
		print(parkSpots.identity, parkSpots.lat, parkSpots.lon)
		if parkSpots.inRange(radius, 
				parkSpots.haversine(parkSpots.lat,lat,parkSpots.lon,lon)):
			inRangeSpots.append({"id": parkSpots.identity, "lat": parkSpots.lat, "lon": parkSpots.lon})
	print(len(inRangeSpots))
	return JsonResponse(inRangeSpots)

def reserve(request):
	pass
	# if(request.POST):
	# 	spot_form = SpotForm(request.POST)
	# 	if(spot_form.isValid()):

	# cust_ID = request.POST.get('id')














