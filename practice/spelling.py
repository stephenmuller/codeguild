"""check if a word follows the I before E rule"""

# setup
ie_check = 'ie'
ei_check = 'ei'
cie_check = 'cie'
# input

word = input('word to check: ')
if word == '':
    word = 'ceiling'

# transform

if ie_check in word:
    if cie_check in word:
        print(word + ' does follow the rule')
    print('wohoo')


else:
    print('ugh.')

# output
