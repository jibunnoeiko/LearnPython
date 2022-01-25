# Activity 10: The Fibonacci Function with an Iteration
# ------------------------------------------------------------------------------



def fibonacci_iterative(n=int(input())):
    # F1 и F2 равны 1
    f1 = f2 = 1
    # Используем цикл for. Looping не должен превышать n, а сам начинается с
    # двух, так как нам известны первые два числа
    for looping in range(2,n):
        formula = f1 + f2
        f1 = f2
        f2 = formula
        # Looping будет увеличиваться пока не будет равен n
        looping += 1
    # Наш результат
    return f2

# Вызов функции
print(fibonacci_iterative())



# Book Solution
def fibonacci_iterative(n):
    previous = 1
    current = 1
    for i in range(2,n):
        current_old = current
        current = previous + current
        previous = current_old
    return current
print(fibonacci_iterative(int(input())))
