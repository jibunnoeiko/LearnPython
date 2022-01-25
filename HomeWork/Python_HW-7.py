# Task 6

# car - 3
# Vlad - 1
# dog - 1
# bus - 2



word_count = {}
def addWord(n):
    global word_count
    if n in word_count:
        word_count[n] += 1
    else:
        word_count[n] = 1

def printAll():
    for k, v in word_count.items():
        print(f'{k} - {v}')

addWord('car')
addWord('Vlad')
addWord('car')
addWord('car')
addWord('bus')
addWord('bus')
addWord('dog')
printAll()
