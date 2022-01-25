# List
# Index begin with 0
#             0              1            2
todo = ['walk with dog', 'wash car', 'check email']

# Dictionary
user = {
    'first name': 'Vlad',
    'last name': 'Henkel',
    'age': 19,
    'hobbies': 'coffee',
    'prof': 'software engineer',
}

shopping = ['bread', 'milk', 'eggs']

for item in shopping:
    print(item)

mixed = [365, 'hello', True]

for item in mixed:
    print(item)
#
result = 0
for n in range(1, 11): # Recall that this loops through 1 to 10, not including 11
    result += n
if __name__ == '__main__':
 print(result)
