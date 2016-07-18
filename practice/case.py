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
<<<<<<< HEAD


    """
    if '_' in user_word:
        case = 'snake_case'
=======
    """
    case = 'snake_case'
    # if '_' in user_word:
    #     case = 'snake_case'
>>>>>>> 7fce879b2bef5f5cfb8a9be9e338330c26ca6b86
    return case


def snake_to_normal_words(snake_word):
    """ takes a weird word and converts it to a normalized format

<<<<<<< HEAD
    >>> snake_to_normal_words(snake_case)
=======
    >>> snake_to_normal_words('snake_case')
>>>>>>> 7fce879b2bef5f5cfb8a9be9e338330c26ca6b86
    ['snake', 'case']
    """
    return snake_word.split(_)


<<<<<<< HEAD
=======
def convert_to_camel(snake_word):
    """ converts the normalized word into CamelCase

    >>> convert_to_camel('snake_word')
    SnakeCase
    """
    snake_list = snake_word.split(_)
    capital_list = [word.capitalize() for word in snake_list]
    camel_case = str.join(capital_list)

>>>>>>> 7fce879b2bef5f5cfb8a9be9e338330c26ca6b86
# def convert_to_camel(word):
#     """converts a word into CamelCase
#
#     >>> convert_to_camel('snake_case')
#     CamelCase
#     """


<<<<<<< HEAD
=======




#
>>>>>>> 7fce879b2bef5f5cfb8a9be9e338330c26ca6b86
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
<<<<<<< HEAD
    camel_case = convert_to_camel(input_words)



main
=======
    camel_case = convert_to_camel(listed_words)


if __name__ == '__main__':
    main()
>>>>>>> 7fce879b2bef5f5cfb8a9be9e338330c26ca6b86
