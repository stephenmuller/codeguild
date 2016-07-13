"""translate cases to other cases"""


def input_words():
    """take user words for proccessing"""
    words = input('what is your word')
    if words == '':
        words = 'snake_case'
    return words


def check_input(user_word):
    """check what case the user submitted

    >>> check_input('snake_case')
    'snake_case'


    """
    if '_' in user_word:
        case = 'snake_case'
    return case


def snake_to_normal_words(snake_word):
    """ takes a weird word and converts it to a normalized format

    >>> snake_to_normal_words(snake_case)
    ['snake', 'case']
    """
    return snake_word.split(_)


# def convert_to_camel(word):
#     """converts a word into CamelCase
#
#     >>> convert_to_camel('snake_case')
#     CamelCase
#     """


# def convert_to_snake(user_word):
#     """ converts to snake case:
#     >>> convert_to_snake()
#
#     """


def main():
    input_words = take_user_words()
    case_type = check_input()
    listed_words = snake_to_normal_words()
    # snake_case = convert_to_snake()
    camel_case = convert_to_camel(input_words)



main
