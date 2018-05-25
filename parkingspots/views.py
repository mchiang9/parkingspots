from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import spots
from . serializers import spotsSerializer
from django.core import serializers
import math

class spotsList(APIView):

	def get(self,request):
		cust_Lat = request.GET.get('lat',0)
		cust_Lon = request.GET.get('lon',0)
		cust_Radius = request.GET.get('radius',0)
		inRangeIDs = []
		for parkSpots in spots.objects.all():
			if (parkSpots.inRange(cust_Radius, 
				parkSpots.haversine(parkSpots.lat,cust_Lat
				,parkSpots.lon,cust_Lon)) == True):
				inRangeIDs.append(parkSpots.identity)


		spots1 = spots.objects.filter(reserved = False 
				, identity__in = inRangeIDs
				 )

		serializer = spotsSerializer(spots1, many= True)
		return Response(serializer.data)


	def post(self,request):
		cust_ID = request.GET.get('id')
		





