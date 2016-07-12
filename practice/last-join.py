# 1. Setup
def input_default(msg, default):
    value = input(msg)
    if '' == value:
        value = default

    return value

def join_words(words):
    word_count = len(words)

    if word_count == 1:
        output = words[0]
    if word_count == 2:
        pair_joiner = input('Joiner: ')
        output = ' ' + pair_joiner + ' '.join(words)
    if word_count >= 3:
        joiner = input('Joiner: ')
        if '' == joiner:
            joiner = ','

        joiner = joiner + ' '

        last_joiner = input_default('Last joiner: ', ', and')
        last_joiner += ' '

        output = last_joiner + words[-1]
        output = joiner.join(words[:-1]) + output

    prefix = str(word_count) + " word"
    if word_count > 1:
        prefix += 's'

    prefix += ': '

    return prefix + output


# 2. Input
input_str = input('Please input a list of words, separated by a space. ')
if '' == input_str:
    input_str = 'apple banana clove frat pain mask asdf what weird face'


# 3. Transform

words = input_str.split()
output = join_words(words)

# 4. Output

print(output)
