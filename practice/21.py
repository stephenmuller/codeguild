"""Gives blackjack advice"""

# I don't understand why the ace should be worth 1 pt
#
#

players_card_second_total = 'none'

# input
print('What is your first card? A 1 2 3 4 5 6 7 8 9 J Q K:   ')
players_card_one = input()
print('What is your second card? A 1 2 3 4 5 6 7 8 9 J Q K:   ')
players_card_two = input()

# transform

if players_card_one == 'A':
    players_card_one_int = 11
elif players_card_one == '1':
    players_card_one_int = 1
elif players_card_one == '2':
    players_card_one_int = 2
elif players_card_one == '3':
    players_card_one_int = 3
elif players_card_one == '4':
    players_card_one_int = 4
elif players_card_one == '5':
    players_card_one_int = 5
elif players_card_one == '6':
    players_card_one_int = 6
elif players_card_one == '7':
    players_card_one_int = 7
elif players_card_one == '8':
    players_card_one_int = 8
elif players_card_one == '9':
    players_card_one_int = 9
elif players_card_one == 'J':
    players_card_one_int = 10
elif players_card_one == 'Q':
    players_card_one_int = 10
elif players_card_one == 'K':
    players_card_one_int = 10


if players_card_two == 'A':
    players_card_two_int = 11
elif players_card_two == '1':
    players_card_two_int = 1
elif players_card_two == '2':
    players_card_two_int = 2
elif players_card_two == '3':
    players_card_two_int = 3
elif players_card_two == '4':
    players_card_two_int = 4
elif players_card_two == '5':
    players_card_two_int = 5
elif players_card_two == '6':
    players_card_two_int = 6
elif players_card_two == '7':
    players_card_two_int = 7
elif players_card_two == '8':
    players_card_two_int = 8
elif players_card_two == '9':
    players_card_two_int = 9
elif players_card_two == 'J':
    players_card_two_int = 10
elif players_card_two == 'Q':
    players_card_two_int = 10
elif players_card_two == 'K':
    players_card_two_int = 10

players_card_initial_total = players_card_one_int + players_card_two_int



if players_card_initial_total > 21 and players_card_two_int == 11:
    players_card_two_int = 1
    players_card_initial_total = players_card_one_int + players_card_two_int

# output
if players_card_initial_total < 17:
    print('You\'re under 17, with a score of:' + str(players_card_initial_total) + ' hit!')
    players_card_three = input('What did you draw? A 1 2 3 4 5 6 7 8 9 J Q K:   ')
    if players_card_three == 'A':
        players_card_three_int = 11
    elif players_card_three == '1':
        players_card_three_int = 1
    elif players_card_three == '2':
        players_card_three_int = 2
    elif players_card_three == '3':
        players_card_three_int = 3
    elif players_card_three == '4':
        players_card_three_int = 4
    elif players_card_three == '5':
        players_card_three_int = 5
    elif players_card_three == '6':
        players_card_three_int = 6
    elif players_card_three == '7':
        players_card_three_int = 7
    elif players_card_three == '8':
        players_card_three_int = 8
    elif players_card_three == '9':
        players_card_three_int = 9
    elif players_card_three == 'J':
        players_card_three_int = 10
    elif players_card_three == 'Q':
        players_card_three_int = 10
    elif players_card_three == 'K':
        players_card_three_int = 10
    players_card_second_total = players_card_one_int + players_card_two_int + players_card_three_int
    if players_card_second_total > 21:
        if players_card_one_int == 11:
            players_card_one_int = 1
        elif players_card_two_int == 11:
            players_card_two_int = 1
        elif players_card_three_int == 11:
            players_card_three_int = 1
            players_card_second_total = players_card_one_int + players_card_two_int + players_card_three_int
    if players_card_second_total > 21:
        print('You went over 21, Bust!')
    elif players_card_second_total == 21:
        print('blackjack!')
    elif players_card_second_total > 16:
        print('Your score is now: ' +
        str(players_card_second_total) + ' You should hold!')
    elif players_card_second_total < 17:
        print('find a different game to play, this is tedious!')



elif players_card_initial_total == 21:
    print('Blackjack!')
elif players_card_initial_total or players_card_second_total >= 17:
    print('You\'re over 17, I reccomend you stay.')

print('\n\n')

# output variables for transparency
print('these are the variable values for testing: ')
print('players_card_one: ' + str(players_card_one_int))
print('players_card_two: ' + str(players_card_two_int))
print('players_card_initial_total: ' + str(int(players_card_initial_total)))
