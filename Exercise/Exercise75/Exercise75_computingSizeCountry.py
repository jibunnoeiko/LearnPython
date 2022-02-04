"""Exercise 75: Computing the Size of Our Country
------------------------------------------------------------------------------"""


class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate=0.6):
        return self.size_kmsq * conversion_rate**2

    # def __str__(self) -> str:
    #     return 'Country: %s\nSize in square miles: %s mi\nPopulation: %s millon\
    #         \n' % (self.name, self.size_kmsq, self.population)


algeria = Country(name='Algeria', population=43.85, size_kmsq=2.382e6)
russia = Country(name='Russia', population=144.1, size_kmsq=17.13)
usa = Country(name='USA', population=329.5, size_kmsq=9.834)
# print(f'\n{algeria}\n{russia}\n{usa}')
print(f'Country: {algeria.name}\nSize in square miles: {algeria.size_miles_sq(0.6)} mi\n\
Population: {algeria.population} millon\n')
print(f'Country: {russia.name}\nSize in square miles: {russia.size_miles_sq(0.6)} mi\n\
Population: {russia.population} millon\n')
print(f'Country: {usa.name}\nSize in square miles: {usa.size_miles_sq(0.6)} mi\n\
Population: {usa.population} millon\n')