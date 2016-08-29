"""polls Views."""

from . import models
from . import logic
from django.http import HttpResponse
from django.shortcuts import render


def render_submission(request):
    """renders the submission page"""
    template_data = {
        'flavors': models.ice_cream_selections
    }
    return render(request, 'polls/submission.html', template_data)


def render_summary(request):
    """renders the summary page"""
    try:
        favorite_ice_creams = [
            [key, "{0:.0f}%".format(value * 100)]
            for key, value
            in logic.flavor_percentages().items()
        ]
    except ZeroDivisionError:
        return HttpResponse('no votes placed', status=400)
    template_data = {
        'favorites': favorite_ice_creams
    }
    return render(request, 'polls/summary.html', template_data)


def render_ack(request):
    """page that loads on successful submission"""
    models.store_poll_result(request.POST['flavor'])
    return render(request, 'polls/ack.html')

