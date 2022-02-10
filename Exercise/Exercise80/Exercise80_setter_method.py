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
        self.celsius = (value - 32) * 5 / 9


temp = Temperature(5)
temp.fahrenheit = 33
print(temp.celsius)