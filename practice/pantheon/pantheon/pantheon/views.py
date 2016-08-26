"""pantheon Views."""

from django.http import HttpResponse
from django.shortcuts import render
from . import models
from . import logic


def index(request):
    """takes the list of countries and creates a view that displays a list of links"""
    template_arguements = {
        'countries': logic.generate_template_obj_for_index,
    }
    return render(request, 'pantheon/index.html', template_arguements)


def all_industries_for_country(request, country_code):
    template_arguements = {
        'industries': logic.generate_template_obj_for_country(country_code),
    }
    return render(request, 'pantheon/country.html', template_arguements)


def persons_in_industry(request, country_code, industry):
    """prints a list of people in a specific country and industry"""
    template_arguements = {
        'people': logic.generate_names_for_industry_page(country_code, industry)
    }
    return render(request, 'pantheon/country_industry.html', template_arguements)


def description_for_person(request, cur_id):
    """Prints information about person"""
    person = models.make_person_object(cur_id)
    template_arguements = {
        'gender': person['gender'],
        'name':person['name'],
        'birth_year': person['birthyear'],
        'country': person['countryName'],
        'occupation': person['occupation']
    }
    return render(request, 'pantheon/person_page.html', template_arguements)


# def render_index(request):
#     """Render the index of all elements."""
#     template_arguments = {
#         'elements': ELEMENTS,
#     }
#     return render(request, 'periodic/index.html', template_arguments)
# ill list of all countries and link each one to the below country listing page.