# Task 2:
def giveMeStart(sentence, character):
        if character in sentence:
            print(sentence[:sentence.index(character)])


giveMeStart('Saa bb cc. Dd ee ff', input('Character: '))
# --> 'Aaa bb cc. '

