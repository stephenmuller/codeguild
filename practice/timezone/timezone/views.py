"""timezone Views."""

import arrow
from django.http import HttpResponse
from . import logic


def display_server_time(request):
    """uses the arrow library to return the time in iso8601 formatting"""
    server_time = arrow.now()
    time_string = 'the time is {}'.format(server_time.isoformat(sep='T'))
    return HttpResponse(time_string)


def display_lat_long_time_zone(request, lat, lng):
    """uses the pytzwhere library"""
    try:
        time_zone = logic.get_timezone_description(float(lat), float(lng))
    except ValueError:
        return HttpResponse('this does not return a time zone, try again', status=404)
    to_display = 'the local area is {}'.format(time_zone)
    return HttpResponse(to_display)

# test url http://localhost:8000/35.29,-89.66/tz


def display_time_by_timezone(request, lat, lng):
    """gets the time based on the time zone"""
    try:
        time = logic.get_time_by_lat_lng(float(lat), float(lng))
    except KeyError:
        return HttpResponse('try again, 400', status=400)
    to_print = 'the time in this timezone is {}'.format(time)
    return HttpResponse(to_print)

# test url http://localhost:8000/35.29,-89.66/time


def display_other_timezone(request, time, lat, lng):
    """starts with a raw time and converts it to the time in another time zone"""
    translated_time = logic.convert_timezone(time, float(lat), float(lng))
    to_display = 'the converted time is {}'.format(translated_time)
    return HttpResponse(to_display)


#test stuff
# 2016-08-25T13:47:29.385017-05:00
# http://localhost:8000/2016-08-25T13:47:29.385017-05:00/at/35.29,-89.66
