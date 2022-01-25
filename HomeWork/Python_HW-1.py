# Page 6-8:  Basic Math Operations
# ------------------------------------
# Try this quickly. Nothing mysterious here.
# The only interesting thing here is modulo operator %
# Task1: Write condition if that prints text "ODD" if the x is odd (3, 5, 7 .... )

# My solution
numbers = (3, 6, 7)
for n in numbers:
    if n % 2 != 0:
        print(f'{n} is odd.')
    else:
        print(f'{n} is even.')


# Mentor solution
numbers = (3, 6, 7)
for n in numbers:
    if n % 2:
        print(f'{n} is odd.')
    else:
        print(f'{n} is even.')


# Task2: Try to create list of three items and assign them to three variables and print them.

# My solution
a, b, c = 8, 5, 3
numbers = [a, b, c]
for n in numbers:
    print(n)
    
# Mentor solution
a, b, c = [10, 20, 30]
print(f'a is: {a}')
print(f'c is: {c}')


# Task3: Write 5 lines and comment out print b and c... with docstring

# My solution
print('a')
""" print 'b' """
print('b')
""" print 'c' """
print('c')
print('d')
print('e')

# Mentor solution
print('a')
'''
print('b')
print('c')
'''
print('e')
print('d')

# Task4: Create function that gets 2 parameters: string and character.
# And return how many same characters are in string without case sensitivity

# My solution
def same_characters(sentence, character):
    sentence, character = sentence.lower(), character.lower()
    print(sentence.count(character), "-", character)
same_characters('Yay, yay', 'y')

# Mentor solution
def same_characters(sentence, character):
    print(sentence.lower().count(character.lower()))


same_characters('Yay, yay', 'y')
