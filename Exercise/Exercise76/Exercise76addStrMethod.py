# Exercise 76 Adding an __str__ Method to the Country Class
# ------------------------------------------------------------------------------


class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self) -> str:
        label = self.name
        if self.population:
            label = '%s, popularion: %s' % (label, self.population)
        if self.size_kmsq:
            label = '%s, size_kmsq: %s' % (label, self.size_kmsq)
        return label


chad = Country(name='Chad', population=1000, size_kmsq=100)
print(chad)


# Before exercise
# class Pet():
#     def __init__(self, height, name) -> None:
#         self.height = height
#         self.name = name

#     is_human = False
#     owner = 'Michael Smith'

#     def __str__(self) -> str:
#         return '%s (height: %s cm)' % (self.name, self.height)


# my_other_pet = Pet(40, 'Rudolf')
# print(my_other_pet)
