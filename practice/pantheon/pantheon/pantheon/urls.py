"""pantheon URL Configuration

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
from . import view


urlpatterns = [
    url(r'^/', view.index, name='index'),
    url(r'^country/(?P<country_code>.+)', view.all_industries_for_country, name='industries_for_country'),
    url(r'^country/(?P<country_code>.+)/industry/(?P<industry>)', view.persons_in_industry, name='persons_in_industry'),
    url(r'^persons/(?P<cur_id>.+', view.description_for_person, name='description_for_person')
]


# We're going to make a web interface for the dataset. Include a static style sheet that styles all of the pages.
#
# GET / will list of all countries and link each one to the below country listing page.
#
# GET /country/COUNTRY_CODE will list all industries known for a country and link each one to the below industry listing page.
#
# GET /country/COUNTRY_CODE/industry/INDUSTRY will list all persons in that industry and link each one to the below person description page.
#
# GET /persons/CUR_ID will show a description page for a specific person. Render a HTML page in a pretty way that displays:
#
# Name
# Birth Year
# Country
# Occupation
# Google Map of Location (include static JS to perform this)
# (Trite, but) have the page style be templated to be pink or blue on the gender of the person


# ?P<symbol>.+)