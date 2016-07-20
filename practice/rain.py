"""Rain
Imports rain data from a portland sensor and analyzes various things.

"""


import statistics

# from itertools import groupby


def import_rain_data_doc():
    """Read file into list of lines."""

    with open('rain_data_easy.txt', newline='') as f:
        lines = f.readlines()
    return lines


def get_relavent_lines(input_doc_string):
    r""" Takes the list of lines and strips off the lines that have no valid data in them.

    >>> get_relavent_lines(['a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'a \n', 'first relevant line', 'second relevant line'])
    [['first relevant line'], ['second relevant line']]
    """

    lines_in_doc = [x.strip().split('\n') for x in input_doc_string]
    lines_of_table = lines_in_doc[11:]
    return lines_of_table


def make_lines_lists(bloated_lines):
    """"Takes the list of lines and turns them into a nested list.

    >>> make_lines_lists([['99-MON-1999 0 0 0 0 0 0 0']])
    [['99-MON-1999', '0', '0', '0', '0', '0', '0', '0']]
    """

    output = []
    for date_strings in bloated_lines:
        output += [z.split() for z in date_strings]
    return output


def purge_unneccessary_data(bloated_lists):
    """Takes the nested lists and returns a nested list with only the date and value.

    >>> purge_unneccessary_data([['99-MON-1999', '0', '0', '0', '0', '0', '0', '0']])
    [['99-MON-1999', '0']]
    """

    output = []
    for x in bloated_lists:
        output += [x[0:2]]
    return output


def convert_to_int(date_rain_pairs):
    """Takes the pairs and converts the rain value to an int for calculating statistics

    >>> convert_to_int([['99-MON-1999', '0'], ['88-MON-1999', '-']])
    [['99-MON-1999', 0]]
    """

    output = []
    for date, rain in date_rain_pairs:
        if rain != '-':
            rain = int(rain)
            output += [[date, rain]]
    return output


def check_for_most_rain(pairs):
    """Returns the date with the most rainfall

    >>> check_for_most_rain([['12-FEB-2002', 5], ['12-MAR-2015', 10]])
    '12-MAR-2015'
    """

    rainfall_to_date_dict = {date_rain[1]: date_rain[0] for date_rain in pairs}
    maximum_rain_per_day = max(rainfall_to_date_dict)
    output = rainfall_to_date_dict[maximum_rain_per_day]
    return output


def calculate_rain_by_year(date_rainfall_list, years_list):
    """Returns a list of years and their total rainfall

    >>> calculate_rain_by_year([['12-FEB-2002', 5], ['12-MAR-2015', 10]], ['2002', '2015'])
    [['2002', 5], ['2015', 10]]
    """

    year_rain_total_list = []
    for year in years_list:
        rainfall_total = 0
        for date, rainfall in date_rainfall_list:
            if year in date:
                rainfall_total += rainfall
        year_rain_total_list += [[year, rainfall_total]]
    return year_rain_total_list


def generate_list_of_days(pairs):
    """generate a list of days given the input document

    >>> generate_list_of_days([['12-FEB-2002', 5], ['12-MAR-2015', 10]])
    ['12-MAR', '12-FEB']
    """

    dates = []
    for date, amount in pairs:
        dates += [date[:6]]
    dates = list(set(dates))
    return dates


def calculate_rain_by_date(date_rain, days_list):
    """calculates the average rainfall by date of the year

    >>> calculate_rain_by_date([['12-FEB-2002', 5], ['12-FEB-2012', 5], ['12-MAR-2015', 10]], ['12-MAR', '12-FEB'])
    {'12-MAR': [10], '12-FEB': [5, 5]}
    """

    list_of_averages = {}
    for day in days_list:
        rain_val_list = []
        for date, rain_inches in date_rain:
            if day in date:
                rain_val_list += [rain_inches]
                list_of_averages.update({day: rain_val_list})
    return list_of_averages


# in progress block to efficiently calculate the rainfall by day of year
# def calculate_rain_by_date(date_rain, days_list):
#     """calculates the average rainfall by date of the year"""
#     date_to_rain_vals = {day: [] for day in days_list}
#     date_to_rain_vals.update({date[:6]: rainfall for date, rainfall in date_rain})
#     print(date_to_rain_vals)
#     return date_to_rain_vals
#
#     date_to_rain_vals = {
#         group_key: list(grouped_items)
#         for group_key, grouped_items
#         # 1. Specify Input
#         in groupby(my_books, get_author)
#      }
#
# def rm_year_from_date(date_rain_pair):
#     """
#     >>> rm_year_from_date(['01-MAR-1998', 54])
#     '01-MAR'
#     """
#     complete_date = date_rain_pair[0]
#     return complete_date[:6]


def calculate_average_rain_by_date(day_rain_dic, days):
    """Finds the average rain by day of year

    >>> calculate_average_rain_by_date({'12-MAR': [10], '12-FEB': [5, 60]}, ['12-MAR', '12-FEB'])
    {32.5: '12-FEB', 10: '12-MAR'}
    """
    avg_dic = {}
    for day in days:
        value_to_avg = day_rain_dic.get(day)
        avg_rain = statistics.mean(value_to_avg)
        avg_dic.update({avg_rain: day})
    return avg_dic


def calculate_highest_average_rain_day(rain_dict):
    """searches the rainfall dict and finds the date with max rain

    >>> calculate_highest_average_rain_day({32.5: '12-FEB', 10: '12-MAR'})
    '12-FEB'
    """
    max_rain = max(rain_dict)
    output = rain_dict.get(max_rain)
    return output


def generate_list_of_years(data_table):
    """Returns a list of the years in the data table.

    >>> sorted(generate_list_of_years([['12-FEB-2002', 5], ['12-MAR-2015', 10]]))
    ['2002', '2015']
    """

    years = [date[7:13] for date, rain in data_table]
    output = (list(set(years)))
    return output


def find_rainiest_year(year_rain_list):
    """ Puts the year and year total value in a dictionary and returns the key of the max value

    >>> find_rainiest_year([['2002', 5], ['2015', 10]])
    '2015'
    """
    
    year_rain_dict = {x[1]: x[0] for x in year_rain_list}
    max_year = max(year_rain_dict)
    val_of_max = year_rain_dict[max_year]
    return val_of_max


# def userio(rain_day_avgs):
#     """ adds user interaction to pull s"""


def output_function(year, day, high_rain_day):
    """Prints the date of the rainiest year and the rainiest day"""

    print('The raniest year at this sensor was: ' + year)
    print('The raniest day at this sensor was: ' + day)
    print('The highest average rainfall is: ' + high_rain_day)
    return


def main():
    """The main function to pull information about Portland rainfall."""

    rainfall_data_dump = import_rain_data_doc()
    data_without_header = get_relavent_lines(rainfall_data_dump)
    data_as_lists = make_lines_lists(data_without_header)
    date_and_rainfall = purge_unneccessary_data(data_as_lists)
    date_rainfall_list = convert_to_int(date_and_rainfall)
    rainiest_date = check_for_most_rain(date_rainfall_list)
    list_of_days = generate_list_of_days(date_rainfall_list)
    rain_by_day = calculate_rain_by_date(date_rainfall_list, list_of_days)
    average_rain_by_date = calculate_average_rain_by_date(rain_by_day, list_of_days)
    highest_average_rainfall_date = calculate_highest_average_rain_day(average_rain_by_date)
    list_of_years = generate_list_of_years(date_rainfall_list)
    total_rain_per_year = calculate_rain_by_year(date_rainfall_list, list_of_years)
    most_rain_in_a_year = find_rainiest_year(total_rain_per_year)
    # userio(average_rain_by_date)
    output_function(most_rain_in_a_year, rainiest_date, highest_average_rainfall_date)


if __name__ == '__main__':
    main()
