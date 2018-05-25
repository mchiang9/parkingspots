from django import forms
from django.forms import ModelForm
from parkingspots.models import spots


class SpotForm(ModelForm):

    class Meta:
        model = spots
        fields=['identity','lat','lon','reserved']