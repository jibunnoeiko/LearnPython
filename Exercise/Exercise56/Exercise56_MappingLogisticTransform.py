# Exercise 56: Mapping with a Logistic Transform
# ------------------------------------------------------------------------------


#            1
# f(x) = ----------
#         1 + e^-x

import math

nums = [-3]
print(list(map( lambda x: 1 / (1 + math.exp(-x)), nums)))
