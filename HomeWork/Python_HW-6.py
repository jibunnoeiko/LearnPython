# Task 5:
# As a result print counts of word > 1:
# the - 7
# their 4
# was - 2
# this - 2
# ------------------------------------------------------------------------------

# We have a text
text = '''aaa AAA aaa aaa aaa Wales greatest moment. Lille is so close to the
Belgian border,
this was essentially a home game for one of the tournament favourites. Their
confident supporters mingled with their new Welsh fans on the streets,
buying into the carnival spirit - perhaps more relaxed than some
might have
been before a quarter-final because they thought this was their time.
In the driving rain, Wales produced the best performance in their history to
carry the nation into uncharted territory. Nobody could quite believe it.'''


words = text.replace('\n',' ').replace('.','').replace(',','').lower().split(' ')

word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1


new_word_count = {}

for word, number in word_count.items():
    if number in new_word_count:
        new_word_count[number] += (f'\n{word} - {number}')
    else:
        new_word_count[number] = (f'{word} - {number}')


for number, word in sorted(new_word_count.items()):
    if number > 1:
        print(new_word_count[number])
