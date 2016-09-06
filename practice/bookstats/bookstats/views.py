"""bookstats Views."""

from django.http import JsonResponse
from django.shortcuts import render
from . import models

def render_index(request):
    """docstring"""
    return render(request, 'bookstats/index.html')


def return_stats(request):
    """docstring"""
    word = request.GET['word']
    word_count = models.get_word_count(word)
    word_frequency = models.get_word_frequency(word)
    json_stats = _convert_stats_to_json_obj(word, word_count, word_frequency)
    return JsonResponse(json_stats)


def _convert_stats_to_json_obj(word, word_count, word_frequency):
    return {
        'word': word,
        'word_count': word_count,
        'word_frequency': word_frequency
    }


