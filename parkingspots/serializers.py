from rest_framework import serializers
from . models import Spot

class spotsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Spot
		fields = {'identity','lat','lon'}