# Exercise 77: Refactoring Instance Methods Using a Static Method
# ------------------------------------------------------------------------------



import datetime
class Diary():
    def __init__(self, birthday, xmas):
        self.birtday = birthday
        self.xmas = xmas

    @staticmethod
    def format_date(date):
        return date.strftime('%d_%b_%y')
    
    def show_birthday(self):
        return self.format_date(self.birtday)
    def show_xmas(self):
        return self.format_date(self.xmas)

my_diary = Diary(datetime.date(2020,5,14), datetime.date(2020,12,25))
print(my_diary.show_birthday())





# Before exercise
class Pet():
    
    def __init__(self, height) -> None:
        self.height = height
    
    is_human = False
    owner = 'Michael Smith'

    @staticmethod
    def owned_by_smith_family():
        return 'Smith' in Pet.owner
nibbles = Pet(100)
print(nibbles.owned_by_smith_family())