"""bookstats Models."""

import re

with open('bookstats/static/bookstats/pg345.txt') as f:
     imported_data = f.read()


input_data = imported_data.split(' ')
BOOK_DATA = []
for word in input_data:
    word_list = list(word)
    updated_word = []
    for char in word_list:
        match_expression = r"([a-zA-Z'])"
        if re.match(match_expression, char):
            updated_word.append(char)
    updated_word = ''.join(updated_word)
    if updated_word != '':
        BOOK_DATA.append(updated_word)

print(BOOK_DATA)


def word_count():
    """counts the words in the list"""
    return len(BOOK_DATA)


def get_word_count(word):
    """returns the number of times the word is used in the book"""
    counter = 0
    for item in BOOK_DATA:
        if item.lower() == word.lower():
            counter += 1
    if counter == 0:
        raise ValueError
    return counter


def get_word_frequency(word):
    """returns the frequency of a word in the book (times used / total words)"""
    instances = get_word_count(word)
    total_words = word_count()
    return instances / total_words
