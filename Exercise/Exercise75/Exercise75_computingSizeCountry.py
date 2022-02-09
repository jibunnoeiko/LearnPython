# Exercise 75: Computing the Size of Our Country
# ------------------------------------------------------------------------------


class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate=0.6):
        return self.size_kmsq * conversion_rate**2

    def __str__(self) -> str:
        return 'Country: %s\nPopulation: %s millon\nSize in square miles: %s\
             mi\n' % (self.name, self.population, self.size_miles_sq())


algeria = Country(name='Algeria', population=43.85, size_kmsq=2.382e6)
russia = Country(name='Russia', population=144.1, size_kmsq=17.13)
usa = Country(name='USA', population=329.5, size_kmsq=9.834)
print(f'{algeria}\n{russia}\n{usa}')
