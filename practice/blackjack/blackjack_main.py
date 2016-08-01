"""Basic Blackjack Logic"""


from card import Card
from hand import Hand
from deck import Deck
from deck import generate_deck
from deck import shuffle_the_deck
from hand import generate_hand
from card import generate_card_value
from hand import calculate_score



FACE_CARDS = 'JQK'
SUITS = ['H', 'D', 'C', 'S']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def add_card_to_hand(existing_hand, deck):
    """adds a card to an existing hand

    # >>> add_card_to_hand(Hand([Card('H', '5'), Card('C', '4')]))
    Hand([Card('H', '5'), Card('C', '4'), Card('S', '5')])
    """
    output = Hand(existing_hand.hand_list + [deck.deck_of_cards.pop()])
    return output


def first_round(player_hand, dealer_hand):
    """plays the first round"""
    print('You have: {} This hand is worth: {}'.format(player_hand, calculate_score(player_hand)))
    print('The dealer is showing {}'.format(dealer_hand.hand_list[0]))
    print('FOR TESTING::::::the dealer score is {}'.format(calculate_score(dealer_hand)))
    return


def ask_player_what_to_do(player_hand, deck):
    """takes user input to steer the game"""
    user_decision = input('Would you like to hit or stay? ')
    if user_decision == 'hit':
        new_hand = hit_till_stay(player_hand, deck)
    else:
        new_hand = player_hand
        print('you stayed')
    return new_hand


def hit_till_stay(player_hand, deck):
    """allows player to hit until they stay or bust"""
    new_hand = add_card_to_hand(player_hand, deck)
    print('your score is {}'.format(calculate_score(new_hand)))
    if calculate_score(new_hand) > 21:
        print('Bust!!!')
    elif calculate_score(new_hand) < 21:
        decision = input('Would you like to hit? ')
        if decision == 'yes':
            new_hand = add_card_to_hand(player_hand, deck)
        else:
            print('you stayed')
    return new_hand


def dealer_logic(dealer_hand, playing_cards):
    """Plays the dealer hand"""
    initial_score = calculate_score(dealer_hand)
    if initial_score > 14:
        dealer_drew = dealer_hand
    while initial_score < 15:
        dealer_drew = add_card_to_hand(dealer_hand, playing_cards)
        initial_score = calculate_score(dealer_drew)
    return dealer_drew



def output_logic(player_hand, dealer_hand):
    """ prints various things based on score"""
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    if player_score == 21:
        print('You have 21! Blackjack!')
    elif player_score > 21:
        print('Bust, you went over 21, better luck next time!')
    elif 21 > player_score > dealer_score:
        print('You won!')
    elif dealer_score > 21 and player_score < 21:
        print('you won!')
    else:
        print('You lose!')
    print('The final score was player {}, and dealer {}.'.format(calculate_score(player_hand), calculate_score(dealer_hand)))


def main():
    """Main"""
    deck = generate_deck(SUITS, RANKS)
    shuffle_the_deck(deck)
    initial_hand = generate_hand(deck)
    initial_dealer_hand = generate_hand(deck)
    first_round(initial_hand, initial_dealer_hand)
    hand_after_hit = ask_player_what_to_do(initial_hand, deck)
    dealer_hand = dealer_logic(initial_dealer_hand, deck)
    output_logic(hand_after_hit, dealer_hand)


main()
