# Exercise 38: The Maximum Number
# ------------------------------------------------------------------------------



lst = [ 8, 4, 2, 7, 3 ]
# Set the maximum variable to 0
maximum = 0

for number in lst:
    # For each number in our list, check whether the number is bigger than the
    # maximum
    if number > maximum:
        # Set the maximum variable so that it is equal to that number
        maximum = number

# maximum is now equal to the largest number in the list.
print(maximum)
