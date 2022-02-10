# Exercise 79: The Full Name Property
# ------------------------------------------------------------------------------


class Person():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        print('Getting...')
        return '%s %s' % (self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        print('Setting...')
        self.first_name = first
        self.last_name = last


customer = Person('Mary', 'Lou')
customer.full_name = 'Jack Sparrow'
print(customer.full_name)


