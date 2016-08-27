"""pantheon Models."""


import csv


with open('pantheon/pantheon.tsv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    TSV_DATA = [person for person in reader]


def generate_countries(array_of_objects):
    """iterates through array returns list of countries"""
    return [dict['countryCode'] for dict in array_of_objects]


def industries_by_country(array_of_objects, country):
    """does things"""
    return [item['industry'] for item in array_of_objects if item['countryCode'] == country]


def people_in_industry(country_code, industry):
    """add complexity"""
    return [
        item
        for item in TSV_DATA
        if item['countryCode'] == country_code if item['industry'] == industry
        ]


def make_person_object(curid):
    """..... """
    for item in TSV_DATA:
        if item['en_curid'] == curid:
            return item


NAMES_TO_CUR_ID = {
    person['name']: person['en_curid']
    for person
    in TSV_DATA
}





# ['en_curid', 'name', 'numlangs', 'birthcity', 'birthstate', 'countryName', 'countryCode', 'countryCode3', 'LAT', 'LON',
#  'continentName', 'birthyear', 'gender', 'occupation', 'industry', 'domain', 'TotalPageViews', 'L_star',
#  'StdDevPageViews', 'PageViewsEnglish', 'PageViewsNonEnglish', 'AverageViews', 'HPI']
# ['307', 'Abraham Lincoln', '131', 'Hodgenville', 'KY', 'UNITED STATES', 'US', 'USA', '37.571111', '-85.738611',
#  'North America', '1809', 'Male', 'POLITICIAN', 'GOVERNMENT', 'INSTITUTIONS', '66145211', '5.801386687', '586914.722',
#  '41477236', '24667975', '504925.2748', '27.93858549']