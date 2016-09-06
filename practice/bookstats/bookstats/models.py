"""bookstats Models."""

import csv

BOOK_AS_LIST = []


with open('static/bookstats/pg345.txt', newline='') as inputfile:
    BOOK_AS_LIST = list(csv.reader(inputfile))


def word_count():
    """counts the words in the list"""
    return len(BOOK_AS_LIST)


def get_word_count(word):
    """returns the number of times the word is used in the book"""
    counter = 0
    for item in BOOK_AS_LIST:
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
