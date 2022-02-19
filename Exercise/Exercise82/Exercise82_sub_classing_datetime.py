# # Exercise 82: Sub-Classing the datetime.date Class
# # ------------------------------------------------------------------------------


# import datetime


# class MyDate(datetime.date):
#     def add_days(self, n):
#         return self + datetime.timedelta(n)


# date = MyDate(2022, 12, 31)
# print(date.add_days(365))


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(self):
        print('Hi, my name is %s' % self.first_name)


class TalkativePerson(Person):
    def speak(self):
        super().speak()
        print('It is a pleasure to meet you!')


john = TalkativePerson('John', 'Tomic')
john.speak()
