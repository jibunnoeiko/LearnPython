# Exercise 83: Overriding Methods Using super()
# ------------------------------------------------------------------------------



import datetime


class Diary:
    def __init__(self, birthday, xmas):
        self.birthday = birthday
        self.xmas = xmas

    @staticmethod
    def format_date(date):
        return date.strftime('%d-%d-%y')

    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_xmas(self):
        return self.format_date(self.xmas)


class CustomDiary(Diary):
    def __init__(self, birthday, xmas, date_format):
        self.date_format = date_format
        super().__init__(birthday, xmas)

    def format_date(self, date):
        return date.strftime(self.date_format)


first_diary = CustomDiary(datetime.date(2018, 1, 1),
    datetime.date(2018, 3, 3), '%d/%b/%Y')
print(first_diary.show_xmas())
