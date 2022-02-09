class Temperature():

    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return f'{self.celsius * 9 // 5 + 32}°F'


temp = Temperature(0)
temp.celsius = -15
del temp.fahrenheit
print(temp.fahrenheit)

class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


house = House(50000.0)
house.price = 40000.0
del house.price
print(house.price)


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 9 // 5 + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)
