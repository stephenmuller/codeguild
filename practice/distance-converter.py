""""Converts distances between unit types"""

# 1. Define


def prompt_for_data():
    """ take in user strings and output usable variables """
    starting_unit = input('Hello. I am a program that converts distances. What is' +
                          'your starting unit of measurement?' +
                          ' Please input; mi, km, ft or m. ')
    distance_in_starting_unit = float(input('What is your distance amount? '))
    output_unit = input('What is your end unit, please input; mi, km, ft or m ? ')
    user_input_list = []
    user_input_list += [starting_unit, distance_in_starting_unit, output_unit]
    return user_input_list

def convert_to_meters(distance_information):
    """"pull the starting unit from the list and outputs the correct conversion factor from starting unit to meters"""
    MI_TO_M = 1609.34
    KM_TO_M = 1000
    FT_TO_M = 0.3048
    starting_unit = distance_information[0]
    distance_in_starting_unit = distance_information[1]
    if starting_unit == 'mi':
        distance_in_converted_unit = MI_TO_M * distance_in_starting_unit
    elif starting_unit == 'km':
        distance_in_converted_unit = KM_TO_M * distance_in_starting_unit
    elif starting_unit == 'ft':
        distance_in_converted_unit = FT_TO_M * distance_in_starting_unit
    else:
        distance_in_converted_unit = distance_in_starting_unit
    return distance_in_converted_unit

def convert_to_output_distance(distance_information, distance_in_meters):
    MI_TO_M = 1609.34
    KM_TO_M = 1000
    FT_TO_M = 0.3048
    output_unit = distance_information[2]
    if output_unit == 'mi':
        distance_in_output_unit = distance_in_meters / float(MI_TO_M)
    elif output_unit == 'km':
        distance_in_output_unit = distance_in_meters / KM_TO_M
    elif output_unit == 'ft':
        distance_in_output_unit = distance_in_meters / FT_TO_M
    else:
        distance_in_output_unit = distance_in_meters
    return distance_in_output_unit

# 2. Main


def main():

    distance_information = prompt_for_data()
    distance_in_meters = convert_to_meters(distance_information)
    output_distance = convert_to_output_distance(distance_information, distance_in_meters)
    output = str(output_distance)
    print('Output: ' + str(output))
    return output

main()
