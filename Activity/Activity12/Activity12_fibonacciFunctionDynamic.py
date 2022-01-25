# Activity 12: The Fibonacci Function with Dynamic Programming
# ------------------------------------------------------------------------------




stored = {1: 1, 2: 1}

def fibonacci_dynamic(n=int(input('Number: '))):
    for i in range(n):
        if n in stored:
            return stored[n]
        else:
            stored[n] = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)
            return stored[n]


print(fibonacci_dynamic())
