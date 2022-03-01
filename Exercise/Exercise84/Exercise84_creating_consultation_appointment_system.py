# # Exercise 84: Creating a Consultation Appointment System
# # -------------------------------------------------------------------------------



# import datetime

# class Person():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# class Adult(Person):
#     def speak(self):
#         print('Hello, my name is %s %s' % self.first_name, self.last_name)


# class Baby(Person):
#     def speak(self):
#         print('Blah blah blah')


# class Calender():
#     def book_appointment(self, date):
#         print('Booking appointment for date %s' % date)


# class OrganizedAdult(Adult, Calender):
#     pass


# class OrganizedBaby(Baby, Calender):
#     pass


# andreas = OrganizedAdult('Andres', 'Gomez')
# andreas.speak()
# andreas.book_appointment(datetime.date(2022, 2, 20))






# class Person():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def speak(self):
#         print('Hello, my name is %s' % self.first_name)

# class TalkativePerson(Person):
#     def speak(self):
#         super().speak()
#         print('It is a pleasure to meet you!')

# john = TalkativePerson('John', 'Tomic')
# john.speak()


class Dog:
    def make_sound(self):
        print('Woof!')
    
class Cat:
    def make_sound(self):
        print('Miaw!')

class DogCat(Dog, Cat):
    def make_sound(self):
        for i in range(3):
            super().make_sound()

my_pet = DogCat()
my_pet.make_sound()