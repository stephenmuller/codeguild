""""This program switches between different cases"""


import re


def take_input():
    """"Takes user input, has some defaults for quick testing."""
    phrase = input('what is your word: ')
    if phrase == '1':
        phrase = 'tester_snake_case_tester'
    elif phrase == '2':
        phrase = 'TesterCamelCaseTester'
    elif phrase == '3':
        phrase = 'tester-kebab-case-tester'
    elif phrase == '4':
        phrase = 'TESTER_CONSTANT_CASE_TESTER'
    return phrase


def type_analyzer(users_string):
    """Isolates what kind of phrase the user has entered.
    >>> type_analyzer('snake_case')
    'in_snake_case'
    """

    if users_string.isupper():
        case_type = 'in_constant_case'
    elif '-' in users_string:
        case_type = 'in_kebab_case'
    elif '_' in users_string:
        case_type = 'in_snake_case'
    else:
        case_type = 'in_camel_case'
    return case_type


def convert_to_normal(complex_str, input_type):
    """Takes the users complicated string and converts it into a simplified list of words
    >>> convert_to_normal('CONSTANT_CASE_TESTER', 'in_constant_case')
    ['constant', 'case', 'tester']

    >>> convert_to_normal('snake_case_tester', 'in_snake_case')
    ['snake', 'case', 'tester']

    >>> convert_to_normal('CamelCaseTester', 'in_camel_case')
    ['camel', 'case', 'tester']

    >>> convert_to_normal('kebab-case-tester', 'in_kebab_case')
    ['kebab', 'case', 'tester']
    """
    if input_type == 'in_snake_case':
        output = complex_str.split('_')
    elif input_type == 'in_camel_case':
        camel_list = list(re.findall('[A-Z][^A-Z]*', complex_str))
        output = [str.lower(word) for word in camel_list]
    elif input_type == 'in_kebab_case':
        output = complex_str.split('-')
    elif input_type == 'in_constant_case':
        converted_to_lowercase = complex_str.lower()
        output = converted_to_lowercase.split('_')

    return output


def convert_to_camel(normal_words):
    """Takes the normal string of words and converts it into CamelCase.
    >>> convert_to_camel(['snake', 'case'])
    'SnakeCase'
    """
    camel_phrase = [str.capitalize(words) for words in normal_words]
    return ''.join(camel_phrase)


def convert_to_snake(users_string):
    """Takes the normal string of words and converts them into snake_case.
    >>> convert_to_snake(['camel', 'case'])
    'camel_case'
    """
    return '_'.join(users_string)


def convert_to_kebab(normal_list):
    """Takes the normal string of words and converts them into kebab-case.
    >>> convert_to_kebab(['test', 'phrase'])
    'test-phrase'
    """
    return '-'.join(normal_list)


def convert_to_constant(neutral_list_words):
    """Takes the normal string of words and converts them into CONSTANT_CASE.
    >>> convert_to_constant(['silly', 'list', 'of'])
    'SILLY_LIST_OF'
    """
    combined = '_'.join(neutral_list_words)
    return combined.upper()


def output_func(str_type, camel_str, snake_str, kebab_str, constant_str):
    """print function"""
    if str_type == 'in_camel_case':
        print('snake_conversion: ' + snake_str)
        print('kebab-convserion: ' + kebab_str)
        print('CONSTANT_CONVERSION: ' + constant_str)
    elif str_type == 'in_snake_case':
        print('CamelConversion: ' + camel_str)
        print('kebab-convserion: ' + kebab_str)
        print('CONSTANT_CONVERSION: ' + constant_str)
    elif str_type == 'in_kebab_case':
        print('CamelConversion: ' + camel_str)
        print('snake_conversion: ' + snake_str)
        print('CONSTANT_CONVERSION: ' + constant_str)
    else:
        print('CamelConversion: ' + camel_str)
        print('snake_conversion: ' + snake_str)
        print('kebab-convserion: ' + kebab_str)


def main():
    """main"""
    user_words = take_input()
    input_type = type_analyzer(user_words)
    neutral_list_words = convert_to_normal(user_words, input_type)
    translation_1 = convert_to_camel(neutral_list_words)
    translation_2 = convert_to_snake(neutral_list_words)
    translation_3 = convert_to_kebab(neutral_list_words)
    translation_4 = convert_to_constant(neutral_list_words)
    output_func(input_type, translation_1, translation_2, translation_3, translation_4)


if __name__ == '__main__':
    main()