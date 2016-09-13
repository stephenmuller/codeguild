"""jokes URL Configuration

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
from . import views


urlpatterns = [
    url(r'^submitjokes', views.input_jokes, name='submission'),
    url(r'^displayjokes', views.display_jokes, name='display'),
    url(r'^ackjoke', views.render_ack, name='ack')
]


# Have a page to submit jokes via a form. A joke has a "setup" and a "punchline" input. Submitted jokes should be
# saved in a global array in your models module.
#
# Have a listing page where jokes are shown. Initially hide all of the punch lines. Then when someone clicks on the setup
# for a joke, reveal the punchline of just that joke.