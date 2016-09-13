"""flutter Logic."""

from .models import Flut

def return_last_10_fluts():
    r"""returns the last 10 fluts to put on the main page

    >>> add_new_flut('text1', '1997-07-16T19:20:30+01:00')
    >>> add_new_flut('text2', '1997-07-16T19:20:30+02:00')
    >>> return_last_10_fluts()
    [Flut(text='text2', time=datetime.datetime(1997, 7, 16, 17, 20, 30, tzinfo=<UTC>)), Flut(text='text1', time=datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>))]
    """
    return Flut.objects.all()[::-1][:10]


def return_10_latest_matches(key):
    """returns the last 10 fluts matching a query from the url

    >>> add_new_flut('text1', '1997-07-16T19:20:30+01:00')
    >>> add_new_flut('text2', '1997-07-16T19:20:30+02:00')
    >>> return_10_latest_matches('text2')
    <QuerySet [Flut(text='text2', time=datetime.datetime(1997, 7, 16, 17, 20, 30, tzinfo=<UTC>))]>
    """
    return Flut.objects.filter(text__contains=key)


def add_new_flut(text, time=None):
    """

    >>> add_new_flut('text', '1997-07-16T19:20:30+01:00')
    >>> Flut.objects.all()[0]
    Flut(text='text', time=datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>))
    """
    if time == None:
        new_flut = Flut(text=text)
        new_flut.save()
    else:
        new_flut = Flut(text=text, time=time)
        new_flut.save()