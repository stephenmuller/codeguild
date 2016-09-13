"""timezone Logic."""

from tzwhere import tzwhere
import arrow

def get_timezone_description(lat, long):
    tz = tzwhere.tzwhere()
    location =  tz.tzNameAt(lat, long)
    if type(location) == str:
        return location
    else:
        raise ValueError


def get_time_by_lat_lng(lat, long):
    time_by_timezone = arrow.now(get_timezone_description(lat,long))
    return time_by_timezone


def convert_timezone(time, lat, long):
    """takes in a time and a time zone, converts the time to the entered time zone"""
    arrow_time = arrow.get(time)
    timezone = get_timezone_description(lat,long)
    return arrow_time.to(timezone)

