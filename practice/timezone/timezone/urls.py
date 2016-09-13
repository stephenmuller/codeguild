"""timezone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^time/', views.display_server_time, name='display_server_time'),
    url(r'^(?P<lat>.+),(?P<lng>.+)/tz', views.display_lat_long_time_zone, name='display_lat_long_time_zone'),
    url(r'^(?P<lat>.+),(?P<lng>.+)/time', views.display_time_by_timezone, name='display_time_by_timezone'),
    url(r'^(?P<time>.+)/at/(?P<lat>.+),(?P<lng>.+)', views.display_other_timezone)
]

#
#
# GET /time returns the current server time
# GET /LAT,LNG/tz returns the timezone at a given latitude and longitude as a short description string (e.g. US/Pacific)
# GET /LAT,LNG/time returns the local time at a given latitude and longitude
# GET /IN_LAT,IN_LNG/IN_TIME/as/OUT_LAT,OUT_LNG returns the time at IN_LAT,IN_LNG when it is IN_TIME at OUT_LAT,OUT_LNG.