"""turn words into pig latin"""
# setup

VOWEL = 'aeiou'

# input
word = input('word to translate: ')
if word == '':
    word = 'apple'

# transform

# fix case issues
no_caps_word = str.lower(word)

# isolate letters to check for vowels
first_letter = no_caps_word[0]
second_letter = no_caps_word[1]

if first_letter in VOWEL:
    pig_latin_word = word + 'yay'

else:
    if second_letter not in VOWEL:
        pig_latin_suffix = first_letter + second_letter + 'ay'
        pig_latin_word = word[2:] + pig_latin_suffix

    else:
        pig_latin_suffix = first_letter + 'ay'
        pig_latin_word = no_caps_word[1:] + pig_latin_suffix

# output
print('Your word in pig latin is: ' + pig_latin_word)
