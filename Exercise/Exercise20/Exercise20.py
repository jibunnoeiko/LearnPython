# Exercise 20: Using for Loops.
# ------------------------------------------------------------------------------

for i in 'Portland':
    print(i)

for i in range(11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(3, 0, -1):
    print(i)

name = 'Vlad'
for i in range(3):
    for i in name:
        print(i)


for num in range(10,100):
    if num % 2 == 0:
        continue
    if num % 3 == 0:
        continue
    if num % 5 == 0:
        continue
    if num % 7 == 0:
        continue
    print(num)
