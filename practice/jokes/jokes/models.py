"""jokes Models."""


_jokes = []


def return_jokes():
    return _jokes


def add_joke(setup, punchline):
    """put a joke in the list
    >>> add_joke('1', '2')
    >>> print(len(_jokes))
    1
    """
    if is_joke_valid(setup, punchline):
        _jokes.append((setup, punchline))
    else:
        raise ValueError


def is_joke_valid(setup, punchline):
    """
    test fields
    >>> is_joke_valid('test', 'test')
    True
    >>> is_joke_valid()('', 'test')
    False
    >>> is_joke_valid('test', '')
    False
    """
    return len(setup) > 0 and len(punchline) > 0
