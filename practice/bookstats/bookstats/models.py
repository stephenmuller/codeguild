"""bookstats Models."""


with open('bookstats/static/bookstats/pg345.txt') as f:
     imported_data = f.read()


BOOK_DATA = imported_data.split(' ')


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
