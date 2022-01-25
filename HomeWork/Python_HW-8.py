# 1. Calculate the multiplication and sum of two numbers
def number(number1, number2):
	product = number1 * number2
	if product < 1000:
		return product
	else:
		return number1 + number2
print(number(30,40))



# 2. Print the sum of the current number and the previous number
print('Printing current and previous number sum in a range(10)')
previous_num = 0
for i in range(10):
	print(f'Current Number {i} Previous Number  {previous_num}  Sum:'
	   f' {i + previous_num}')
	previous_num = i



# 3. Print characters from a string that are present at an even index number
userInput = input('Input: ')
print(f'Orginal String is {userInput}\nPrinting only even index chars')
for n in range(len(userInput)):
	if n % 2 == 0:
		print(userInput[n])



# 4. Remove first n characters from a string
# ToDo:
#  1. У меня есть строка "pynative".
#  2. Для начала задать тип list() для строки, превратив каждую букву в отдельный
#  элемент.
#  3. Далее задать "n" меньше длины строки.
#  4. Далее написать условие при котором удаляется то кол-во "n", которое было
#  задано, использовать для этого slice syntax.
#  5. Вывести оставшиеся буквы. Например, если "n = 4", то "s = tive".
def remove_chars(s=input('Enter string: '), n=int(input('Enter number: '))):
	return s[n:]

print(f'String: {remove_chars()}')



# 5. Check if the first and last number of a list is the same
# Example:
#      numbers_x => [10, 20, 30, 40, 10] => result is True
#      numbers_y => [75, 65, 35, 75, 30] => result is False
# Todo:
#  1. Создать функцию с двумя списками - "numbers_x" и "numbers_y".
#  2. В одном из списков 1-ое и последнее число будут одинаковыми, а в другом
#  разными.
#  3. Элементы внутри списков будут обозначенны как "n".
#  4. Задать условие при котором, если внутри списка [0:] и [:n] равны,
#  то программа выдает след результат - "result is True", если не равны,
#  то результат меняется на - "result is False".
#  *5. Оптимизировать программу на повторение не только первого и последнего
#  элемента, но и вообще на то, есть ли одинаковые элементы внутри списка.
def first_last_number(numbers):
	if numbers[0] == numbers[-1]:
		return f'result is {True}'
	else:
		return f'result is {False}'


print(first_last_number([10, 20, 30, 40, 10]))
print(first_last_number([75, 65, 35, 75, 30]))

def first_last_number(lst_numbers):
	first_num = lst_numbers[0]
	last_num = lst_numbers[-1]

	if first_num == last_num:
		return True
	else:
		return False

number_x = [10, 20, 30, 40, 10]
print('result is', first_last_number(number_x))
number_y = [75, 65, 35, 75, 30]
print('result is', first_last_number(number_y))



# 6. Display numbers divisible by 5 from a list
# ToDo:
#  1. Создать функцию "funLst" с переменной "lst"
#  2. Задать условие, если элемент делиться на 5, то вывести его, а если нет,
#  то не выводить.

def funLst(lst):
	for n in range(len(lst)):
		if lst[n] % 5:
			print(lst[n])

print('Given list is [10, 20, 33, 46, 55]\nDivisible by 5')
funLst([10, 20, 33, 46, 55])



# 7. Return the count of a given substring from a string
# ToDo:
#  1. Объявить функцию (count_w)
#  2. Внутри функции объявить переменную (sentence)
#  3. После внутри функции объявить переменную (c_words), которая будет хранить
#  число, которое обозначает сколько раз слово повторялось в (sentence),
#  значение по умолчанию 0.
#  4.
#  ...

# With count() method.
str_x = "Emma is good developer. Emma is a writer"
print(f'Emma appeared {str_x.count(input("Enter word: "))} times')

# Without count() method.
word = input('Word: ')
number = int(input('Number: '))
def count_w(sentence):
	global new_word
	c_words = 0
	for n in range(len(sentence)-1):
		c_words += sentence[n: n + number] == word
	return c_words

c_words = count_w('Emma is good developer. Emma is a writer')
print(f'{word} => {c_words}')


# Without count() method.
def count_w(sentence):
	word = sentence.replace('.','').lower().split(' ')
	dictionary_words = {}

	for w in word:
		if w in dictionary_words:
			dictionary_words[w] += 1
		else:
			dictionary_words[w] = 1
	for key, value in dictionary_words.items():
		result = f"{key} => {value}"
		print(result)

count_w("Emma is good developer. Emma is a writer")



# 8. Print the following pattern

# Example:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# ---------
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5


# ToDo:
#  1. Принять инфу по строкам от юзера с помощью (input()).
#  2. Далее с помощью цикла (for) итерируем кол-во строк, добавляем (range(
#  something + 1)).
#  3. Затем добавляем внутренний цикл (for) для итерации столбцов.
#  4. Используем функцию (print) для вывода результата на экран.
#  5. Все.

# reverse pyramid
user_rows = int(input('Rows: '))
reverse_row = 0
for a in range(user_rows, 0, -1):
	reverse_row += 1
	for b in range(1, a + 1):
		print(reverse_row, end=' ')
	print('')

# not reverse pyramid
user_rows = int(input('Rows: '))
for a in range(user_rows):
	for b in range(a):
		print(a, end=' ')
	print('')

# not reverse pyramid
row = 5
for i in range(row, 0, -1):
	i = str(i) * i
	print(i)



# 9. Check Palindrome Number
# ToDo
#  1. Объявить функцию (palindrome_num) для ввода числа палиндрома
#  2. Объявить переменную (reverse_num) для сохранения перевернутых чисел
#  3. Использовать условие (if) для проверки введеного числа и перевернутого

def palindrome_num(number=int(input('Number: '))):
	num = number
	reverse_num = 0
	while number:
		remainder_division = number % 10
		reverse_num = reverse_num * 10 + remainder_division
		number = number // 10
	if num == reverse_num:
		print(f'{num} is a palindrome!')
	else:
		print(f'{num} is not a palindrome!')

palindrome_num()



# 10. Create a new list from a two list using the following condition
# ToDo:
#  1. Довольно легкий таск, расписывать его не имеет никакого значения


lst1 = [10, 20, 25, 30, 35]
lst2 = [40, 45, 60, 75, 90]
lst_result = []

for n in range(len(lst1)):
	if lst1[n] % 2 != 0:
		lst_result.append(lst1[n])

for n in range(len(lst2)):
	if lst2[n] % 2 == 0:
		lst_result.append(lst2[n])


print(f'result list: {lst_result}')



# 11. Write a Program to extract each digit from an integer in the reverse order
# Example: 7536 => 6 3 5 7

# Todo:
#  1. Создать переменную (num) для хранения числа
#  2. Далее цикл (while) с условием (num > 0)
#  3. Объявляем переменную (div), которая будет вычислять остаток от деления
#  (num % 10)
#  4. Далее с каждым пробегом по циклу переменная (num) будет делиться на 10
#  до тех пор пока не будет равна 0
#  5. Выводим результат который получился с помощью (print()) в переменной (
#  div)

num = 7356
while num > 0:
	div = num % 10
	num = num // 10
	print(div, end=" ")



# 12.  Calculate income tax for the given income by adhering to the below rules
# Example: (10000 * 0% + 10000 * 10% + 25000 * 20% = 6000 долларов США.)
# Todo:
#  1. Во перых я объявлю переменную (revenue), которая будет хранить доход.
#  Я не буду брать какое-то определенное число, применю метод (int(input()))
#  2. Далее я создам переменную (taxable_revenue), которая будет помогать
#  определить ставку для суммы
#  3. После я начну создавать условия. Например, если (revenue) меньше
#  10.000$, то (taxable_revenue) равно 0%, от 20.000 (taxable_revenue) равно
#  10%, больше 20.000$ (taxable_revenue) равно 20%, но мы вычитаем первые
#  20.000$, затем оставшиеся деньги умножаем на 20% и добавим 1000$
#  4. Выводим результат наших стараний

revenue = int(input('Enter revenue: '))
print(f'Our revenue: {revenue}')
taxable_revenue = 0

if revenue <= 10000:
	taxable_revenue = 0
elif revenue <= 20000:
	taxable_revenue = (revenue - 10000) * 0.1
else:
	taxable_revenue = (revenue - 20000) * 0.2

print(f'Our tax: {taxable_revenue}')



# 13. Print multiplication table form 1 to 10
# ToDo:
#  1. Создать внешний (for) цикл с диапозоном от 1 до 10
#  2. Создать внутренний (for) цикл с диапозоном 10
#  3. Умножать каждое число 1 * 1, 1 * 2, 1 * 3, 1 * 4 и т.д.


for i in range(1,11):
	for j in range(1,11):
		result = i * j
		print(result, end=' ')
	print('')



# 14. Print downward Half-Pyramid Pattern with Star (asterisk)
# ToDo:
#  1. Задание похоже на предыдущее, единственное что я заменил это (print),
#  вместо названия переменной я записал (*)

user_rows = int(input('Enter quantity of stars: '))

for i in range(user_rows, 0, -1):
	for j in range(0, i):
		print('*', end=' ')
	print('')



# 15.Write a function called exponent(base, exp) that returns an int value of
# base raises to the power of exp.
# ToDo:
#  1. Вернуть значение переменных (base, exp), а также (base) возведенную в
#  степень (exp)

def exponent(base=int(input('Base number: ')), exp=int(input('Exponent: '))):
	return f'base: {base}\n' \
		   f'exponent: {exp}\n' \
		   f'{base} raises to the power of {exp} is: {base**exp}\n'

print(exponent())
