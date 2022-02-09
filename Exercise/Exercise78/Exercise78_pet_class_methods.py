# Exercise 78: Extending Our Pet Class with Class Methods
# ------------------------------------------------------------------------------



import random

class Pet():
    def __init__(self, height) -> None:
        self.height = height

    is_human = False
    owner = 'Michael Smith'

    @classmethod
    def owned_by_smith_family(cls):
        return 'Smith' in cls.owner

    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0,100)
        return cls(height)
    
for i in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height)

    

# Before exercise
class Australian():
    is_human = True
    enjoys_sport = True

    @classmethod
    def is_sporty_human(cls):
        return cls.is_human and cls.enjoys_sport

print(Australian.is_sporty_human())



# Before exercise
class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None) -> None:
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    @classmethod
    def create_with_msq(cls, name, population, size_msq):
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, population, size_kmsq)

mexico = Country.create_with_msq('Mexico', 150e6, 760000)
print(mexico.size_kmsq)