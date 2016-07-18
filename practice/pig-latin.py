"""Turn words into pig latin"""


def get_word():
    """Requests word from user."""
    word = input('word to translate: ')
    if word == '':
        word = 'String'
    return word


def analyze_for_capitals(user_word):
    """Checks word for capital letters to set the output"""
    if user_word[0].isupper():
        capital = True
    else:
        capital = False
    return capital


def check_for_vowels(user_word):
    """Checks word for vowels, returns how many letters need to be moved"""

    VOWEL_STRING = 'aeiou'
    user_word = user_word.lower()
    if user_word[0] in VOWEL_STRING:
        letters_to_move = 0
    elif user_word[:2] not in VOWEL_STRING:
        letters_to_move = 3
    elif user_word[:1] not in VOWEL_STRING:
        letters_to_move = 2
    elif user_word[0] not in VOWEL_STRING:
        letters_to_move = 1
    return letters_to_move


def pig_latin_generator(user_word, capital_information, letters_to_move):
    """Converts the users word into pig latin"""

    if letters_to_move == 0:
        pig_latin_word = user_word + 'yay'
    else:
        if letters_to_move == 2:
            pig_latin_suffix = user_word[:letters_to_move] + 'ay'
            pig_latin_word = user_word[letters_to_move:] + pig_latin_suffix
        elif letters_to_move == 3:
            pig_latin_suffix = user_word[:letters_to_move] + 'ay'
            pig_latin_word = user_word[letters_to_move:] + pig_latin_suffix
        else:
            pig_latin_suffix = user_word[:letters_to_move] + 'ay'
            pig_latin_word = user_word[letters_to_move:] + pig_latin_suffix
    if capital_information is True:
            pig_latin_word = pig_latin_word.capitalize()
    return pig_latin_word


def main():
    """Convert words to pig latin."""
    user_word = get_word()
    capital_information = analyze_for_capitals(user_word)
    letters_to_move = check_for_vowels(user_word)
    pig_latin_word = pig_latin_generator(user_word, capital_information, letters_to_move)
    print(pig_latin_word)

if __name__ == '__main__':
    main()
