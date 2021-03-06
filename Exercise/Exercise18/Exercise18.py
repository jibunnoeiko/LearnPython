# Exercise 18: Calculating Perfect Squares

# Предложите пользователю ввести число, чтобы проверить, является ли оно идеальным квадратом:
print('Enter a number to see if it\'s a perfect square.')
# Установите переменную равной input(). В данном случае введем 64:
# Убедитесь, что введенное пользователем число является целым положительным числом:
number = abs(int(input()))
# Выберите переменную-итератор:
i = -1
# Инициализируйте булево значение для проверки идеального квадрата:
square = False
# Инициализируйте цикл while от -1 до квадратного корня из числа:
while i <= number**(0.5):
    # Увеличьте i на 1:
    i += 1
    # Проверьте квадратный корень из числа:
    if i*i == number:
        # Укажите, что у нас есть совершенный квадрат:
        square = True
        # выйти из цикла:
        break
# Если число квадратное, выведите результат:
if square:
    print('The square root of', number, 'is', i, '.')
# Если число не является квадратом, выведите результат:
else:
    print('', number, 'is not a perfect square.')
# ------------------------------------------------------------------------------
