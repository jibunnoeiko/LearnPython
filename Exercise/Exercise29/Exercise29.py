# Exercise 29: Using the zip() Method to Manipulate Dictionaries
# ------------------------------------------------------------------------------

items = ['apple','orange','banana']

quantity = [5,3,2]

orders = zip(items,quantity)
print(orders)

# also with tuple() и dict()
print(set(orders))

for order in orders:
    print(order)
