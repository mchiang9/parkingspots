from rest_framework import serializers
from . models import spots

class spotsSerializer(serializers.ModelSerializer):

	class Meta:
		model = spots
		fields = {'identity','lat','lon'}