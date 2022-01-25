# Exercise 71 Creating a Pet Class
# ------------------------------------------------------------------------------



class Pet():
    """
    A class to capture useful info regarding my pets, just incase
    I lose track of them
    """
    def __init__(self, height):
        self.height = height

    is_human = False
    owner = 'Michael Smith'
chubbles = Pet(height=5)
print(f'{chubbles.is_human}\nOwner: {chubbles.owner}\nHeight: '
      f'{chubbles.height}{chubbles.__doc__}')



# Before the exercise
# ----------------------------------------------------------------------------
class Australian():
    is_human = True
    enjoys_sport = True

john = Australian()
print(f'Type is: {type(john)}\nIs he human: {john.is_human}\nDoes he en'
      f'joy sport: {john.enjoys_sport}')
# ----------------------------------------------------------------------------
