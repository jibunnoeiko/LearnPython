# Exercise 73: The Country Class with Keyword Arguments
# ------------------------------------------------------------------------------



class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq
usa = Country(name='United States of America', size_kmsq=9.8e6)
print(usa.__dict__)




# ------------------------------------------------------------------------------
# Before exercise:
def function_name(thing, thang = 4):
#                 "arg"    "kwarg"
    print('...')

# Example:
class Circle():
    is_shape = True

    def __init__(self, radius, color='red'):
        self.radius = radius
        self.color = color
my_circle = Circle(23)
print(my_circle.color, my_circle.radius)
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# After exercise:
import math

class Circle():
    is_shape = True

    def __init__(self, radius, color='red'):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(3)
circle.radius = 2
print(f'Area of a circle: {circle.area()}')
# ------------------------------------------------------------------------------
