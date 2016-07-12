"""Gives blackjack advice"""


###investigate else branches and ranges more

# input
print('What is your first card? A 2 3 4 5 6 7 8 9 J Q K:   ')
card_one = input()

print('What is your second card? A 2 3 4 5 6 7 8 9 J Q K:   ')
card_two = input()

# transform

if card_one == 'A':
    points_one = 11
elif card_one == 'J' or card_one == 'Q' or card_one == 'K':
    points_one = 10
else:
     points_one = int(card_one)


if card_two == 'A':
    points_two = 11
elif card_two == 'J' or card_two == 'Q' or card_two == 'K':
    points_two = 10

else:
    points_two = int(card_two)

initial_score = points_one + points_two

if initial_score == 22:
    card_two = 1

final_score = points_one + points_two

#output

if final_score == 21:
    print('Blackjack!')
elif final_score < 17:
    print('Hit!')
else:
    print('hold!')

# #variable checks
# print(type(final_score))
# print(str(final_score))
