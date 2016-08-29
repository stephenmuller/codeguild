"""polls Models."""

ice_cream_selections = {
    'vanilla' : 0,
    'chocolate': 0,
    'strawberry': 0
}


def store_poll_result(flavor):
    """Saves a poll result to the ice_cream_selections dict in models"""
    ice_cream_selections[flavor] += 1