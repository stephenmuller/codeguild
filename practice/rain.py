"""Rain
Imports rain data from a portland sensor and analyzes various things.

"""


import statistics


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group] += [item[1]]
    return group_to_items


def key(list):
    """generates the keys for group_by

    >>> key(['12-MAR-2015', 5])
    '2015'
    """
    temp = list[0]
    temp_2 = temp[7:]
    return temp_2


def date_key(date_rain_list):
    """Returns the first 7 characters of the date structure, 12-MAR
    >>> date_key(['12-MAR-2015', 5])
    '12-MAR'
    """
    temp_1 = date_rain_list[0]
    temp_2 = temp_1[:6]
    return temp_2


def import_rain_data_doc():
    """Read file into list of lines."""
    with open('rain_data.txt', newline='') as f:
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
    output = [z.split() for date_strings in bloated_lines for z in date_strings]
    return output


def purge_unneccessary_data(bloated_lists):
    """Takes the nested lists and returns a nested list with only the date and value.

    >>> purge_unneccessary_data([['99-MON-1999', '0', '0', '0', '0', '0', '0', '0']])
    [['99-MON-1999', '0']]
    """
    output = [x[0:2] for x in bloated_lists]
    return output


def convert_to_int(date_rain_pairs):
    """Takes the pairs and converts the rain value to an int for calculating statistics

    >>> convert_to_int([['99-MON-1999', '0'], ['88-MON-1999', '-']])
    [['99-MON-1999', 0]]
    """
    output = [[date, int(rain)] for date, rain in date_rain_pairs if rain != '-']
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


def calculate_rain_by_year(date_rainfall_list):
    """Returns a list of years and their total rainfall

    >>> calculate_rain_by_year([['12-FEB-2002', 5], ['12-MAR-2015', 10], ['13-MAR-2015', 12]])
    {'2015': [10, 12], '2002': [5]}
    """
    return group_by(date_rainfall_list, key)


def calculate_rain_by_date(date_rain):
    """calculates the average rainfall by date of the year

    >>> calculate_rain_by_date([['12-FEB-2002', 5], ['12-FEB-2012', 5], ['12-MAR-2015', 10]])
    {'12-MAR': [10], '12-FEB': [5, 5]}
    """

    return group_by(date_rain, date_key)




def calculate_average_rain_by_date(day_rain_dict):
    """Finds the average rain by day of year

    >>> calculate_average_rain_by_date({'12-MAR': [10], '12-FEB': [5, 60]})
    {32.5: '12-FEB', 10: '12-MAR'}
    """
    for day in day_rain_dict:
        day_rain_dict[day] = statistics.mean(day_rain_dict[day])
    return day_rain_dict


def calculate_highest_average_rain_day(rain_dict):
    """searches the rainfall dict and finds the date with max rain

    # >>> calculate_highest_average_rain_day({32.5: '12-FEB', 10: '12-MAR'})
    '12-FEB'
    """
    temp_rain = 0
    temp_date = ''
    for day in rain_dict:
        if rain_dict[day] > temp_rain:
            temp_rain = rain_dict[day]
            temp_date = day
    return temp_date


def find_rainiest_year(year_rain_dict):
    """ Puts the year and year total value in a dictionary and returns the key of the max value

    >>> find_rainiest_year({'2002': [5], '2015': [10]})
    '2015'
    """

    for year in year_rain_dict:
        year_rain_dict[year] = sum(year_rain_dict[year])
    max_rain_temp = 0
    max_rain_year_temp = ''
    for year in year_rain_dict:
        if year_rain_dict[year] > max_rain_temp:
            max_rain_temp = year_rain_dict[year]
            max_rain_year_temp = year
    return max_rain_year_temp




def output_function(year, day, high_rain_day):
    """Prints the date of the rainiest year and the rainiest day

    >>> output_function('1992', '25-MAR-2132', '13-MAR')
    The raniest year at this sensor was: 1992
    The raniest day at this sensor was: 25-MAR-2132
    The highest average rainfall is: 13-MAR
    """
    print('The raniest year at this sensor was: ' + year)
    print('The raniest day at this sensor was: ' + day)
    print('The highest average rainfall is: {}'.format(high_rain_day))
    return


def main():
    """The main function to pull information about Portland rainfall."""
    rainfall_data_dump = import_rain_data_doc()
    data_without_header = get_relavent_lines(rainfall_data_dump)
    data_as_lists = make_lines_lists(data_without_header)
    date_and_rainfall = purge_unneccessary_data(data_as_lists)
    date_rainfall_list = convert_to_int(date_and_rainfall)
    rainiest_date = check_for_most_rain(date_rainfall_list)
    rain_by_day = calculate_rain_by_date(date_rainfall_list)
    average_rain_by_date = calculate_average_rain_by_date(rain_by_day)
    highest_average_rainfall_date = calculate_highest_average_rain_day(average_rain_by_date)
    total_rain_per_year = calculate_rain_by_year(date_rainfall_list)
    most_rain_in_a_year = find_rainiest_year(total_rain_per_year)
    output_function(most_rain_in_a_year, rainiest_date, highest_average_rainfall_date)


if __name__ == '__main__':
    main()
