"""jokes Views."""

from django.http import HttpResponse
from django.shortcuts import render
from . import models


def display_jokes(request):
    """takes entry of jokes"""
    template_data = {
        'joke_list': models.return_jokes()
    }
    print(template_data['joke_list'])
    return render(request, 'jokes/displayjokes.html', template_data)


def input_jokes(request):
    """adds the setup/punchline to the array"""
    return render(request, 'jokes/inputjokes.html')


def render_ack(request):
    """adds joke to the psuedo database and presents a page acknowledging submission"""
    try:
        buildup = request.POST['buildup']
        punchline = request.POST['punchline']
    except KeyError:
        return HttpResponse('missing part of your joke', status='400')
    models.add_joke(buildup, punchline)
    return render(request, 'jokes/ack.html')

