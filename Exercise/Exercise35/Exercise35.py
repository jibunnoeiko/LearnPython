# Exercise 35: Writing and Importing Our First Module
# ------------------------------------------------------------------------------



# include math library for factorial function
import math

# create new function and called it compute, include numbers variable
# then we running this script in TERMINAL:
# from Exercise35 import compute
# compute([5,7,11])
def compute(numbers):
    return [math.factorial(n) for n in numbers]


