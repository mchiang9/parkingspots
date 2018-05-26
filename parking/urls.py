"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from parkingspots import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'spots/',views.SpotList.as_view()),
    # re_path(r'^api/v1/parkingspots/available/(?P<lat>[-0-9\.])/(?P<lon>[-0-9\.])/(?P<radius>[0-9\.])/',views.available),
    # re_path(r'^spots/(?P<lat>[-0-9\.])/(?P<lon>[-0-9\.])/(?P<radius>[0-9\.])/', views.spotsList.available)
    # re_path(r'^api/v1/parkingspots/available/(?P<lat>[-0-9\.])/(?P<lon>[-0-9\.])/(?P<radius>[0-9\.])/$',views.available)
    re_path(r'^api/v1/parkingspots/available/(?P<lat>[-0-9\.]+)/(?P<lon>[-0-9\.]+)/(?P<radius>[0-9\.]+)$',views.available)
]
