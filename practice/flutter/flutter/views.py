"""flutter Views."""
from . import models
from django.shortcuts import render
from . import logic

def index(request):
    last_10 = logic.return_last_10_fluts()
    template_data = {
        'fluts': last_10
    }
    return render(request, 'flutter/index.html', template_data)


def query_text(request):
    search = request.POST['search']
    matches_query = logic.return_10_latest_matches(search)
    template_data = {
        'fluts': matches_query
    }
    return render(request, 'flutter/query_text.html', template_data)


def post_flut(request):
    return render(request, 'flutter/post_flut.html')


def post_submit(request):
    new_flut = request.POST['flut_body']
    logic.add_new_flut(new_flut)
    return render(request, 'flutter/post_submit.html')
