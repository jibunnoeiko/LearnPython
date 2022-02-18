# Exercise 80: Writing a Setter Method
# ------------------------------------------------------------------------------

class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -460:
            raise ValueError('Temperatures less than -460F are not possible')
        self.celcius = (value - 32) * 5 / 9

temp = Temperature(5)
temp.fahrenheit = -460 # ValueError: Temperatures less than -460F are not
# possible
print(temp.celcius)


# After exercise
class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Cat(Pet):
    is_feline = True


class Dog(Pet):
    is_feline = False

my_cat = Cat('Sultan', 20)
print(my_cat.name)
