"""check if a word follows the I before E rule"""

# setup
ie_check = 'ie'
ei_check = 'ei'
cie_check = 'cie'
cei_check = 'cei'
# input

word = input('word to check: ')
if word == '':
    word = 'believe'

# transform

if ie_check in word and cie_check not in word:
    follows_rule = True
    # print('yay!')  # test print
elif cei_check in word:
    follows_rule = True
    # print('yay2!')  # test print
else:
    follows_rule = False
    # print('nope')  # test print

# output

if follows_rule is True:
    print(word + ' does follow the rule')

else:
    print(word + ' doesn\'t follow the rule')
