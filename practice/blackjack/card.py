"""card class"""

FACE_CARDS = 'JQK'
SUITS = ['H', 'D', 'C', 'S']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    """A class for representing a card in blackjack"""

    def __init__(self, suit, rank,):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        return(
            self.suit == other.suit and
            self.rank == other.rank
        )

    def __repr__(self):
        return 'Card({!r}, {!r})'.format(
            self.suit,
            self.rank
        )

def generate_card_value(card_to_score):
    """assigns the value of a card does not calculate Ace based on overall score

    >>> generate_card_value(Card('H', '7'))
    7

    >>> generate_card_value(Card('H', 'A'))
    11

    >>> generate_card_value(Card('H', 'A'))
    11
    >>> generate_card_value(Card('H', 'K'))
    10
    """
    if card_to_score.rank in FACE_CARDS:
        card_value = 10
    elif card_to_score.rank == 'A':
        card_value = 11
    else:
        card_value = int(card_to_score.rank)
    return card_value
