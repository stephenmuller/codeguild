"""Hand class"""

from card import Card
from deck import Deck
from card import generate_card_value
from deck import draw_card_from_deck

class Hand:
    """A class for storing blackjack hands"""

    def __init__(self, hand_list):
        self.hand_list = hand_list

    def __eq__(self, other):
        """Return eq

        >>> (
        ... Hand([Card('H', '5'), Card('C', '2')]) ==
        ... Hand([Card('H', '5'), Card('C', '2')])
        ... )
        True

        >>> (
        ... Hand([Card('H', '5'), Card('C', '3')]) ==
        ... Hand([Card('H', '5'), Card('C', '2')])
        ... )
        False
        """
        return(
            self.hand_list == other.hand_list
        )

    def __repr__(self):
        """Return repr.

        >>> repr(Hand([Card('H', '5'), Card('C', '2')]))
        "Hand([Card('H', '5'), Card('C', '2')])"
        """
        return 'Hand({!r})'.format(
            self.hand_list
        )


def generate_hand(deck):
    """adds a card to a hand

    >>> generate_hand(Deck([Card('H', '7'), Card('H', '8')]))
    Hand([Card('H', '8'), Card('H', '7')])
    """
    return Hand([draw_card_from_deck(deck), draw_card_from_deck(deck)])


def calculate_score(hand_to_score):
    """calculates the value of a hand of cards

    >>> calculate_score(Hand([Card('H', '5'), Card('C', '4')]))
    9
    """
    list_of_values = []
    for x in hand_to_score.hand_list:
        list_of_values += [generate_card_value(x)]
    interim_total = sum(list_of_values)
    if interim_total > 21 and 11 in list_of_values:
            interim_total -= 10
    return interim_total
