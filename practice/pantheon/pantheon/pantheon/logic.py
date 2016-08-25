"""pantheon Logic."""

import csv

def dump_tsv():
    with open('pantheon/pantheon.tsv', newline='') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t', quotechar='|')
        for row in reader:
            print(row)



#
# ['en_curid', 'name', 'numlangs', 'birthcity', 'birthstate', 'countryName', 'countryCode', 'countryCode3', 'LAT', 'LON',
#  'continentName', 'birthyear', 'gender', 'occupation', 'industry', 'domain', 'TotalPageViews', 'L_star',
#  'StdDevPageViews', 'PageViewsEnglish', 'PageViewsNonEnglish', 'AverageViews', 'HPI']
# ['307', 'Abraham Lincoln', '131', 'Hodgenville', 'KY', 'UNITED STATES', 'US', 'USA', '37.571111', '-85.738611',
#  'North America', '1809', 'Male', 'POLITICIAN', 'GOVERNMENT', 'INSTITUTIONS', '66145211', '5.801386687', '586914.722',
#  '41477236', '24667975', '504925.2748', '27.93858549']