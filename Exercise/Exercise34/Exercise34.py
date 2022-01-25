# Exercise 34: Writing and Executing Our First Script
# ------------------------------------------------------------------------------


# include math library for factorial function
import math

# create the new list
numbers = [5,7,11]

# 'result' variable calculates the factorial of our numbers in the list
result = sum([math.factorial(n) for n in numbers])
print(result)
