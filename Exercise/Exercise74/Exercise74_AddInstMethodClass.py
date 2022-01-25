# Exercise 74: Adding an Instance Method to Our Pet Class
# ------------------------------------------------------------------------------



class Pet():

    def __init__(self, height):
        self.height = height

    is_human = False
    owner = 'Michael Smith'

    def is_tall(self, tall_if_at_least=60):
        return self.height >= tall_if_at_least

bowser = Pet(50)
print(f'- Bowser is tall?\n'
      f'- {bowser.is_tall(50)}\n')
