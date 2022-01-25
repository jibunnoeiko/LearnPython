# Activity 11: The Fibonacci Function with Recursion
# -----------------------------------------------------------------------------



# # # My solution
# def fibonacci_iterative(n=int(input())):
#     f1 = f2 = 1
#     for looping in range(2,n):
#         formula = f1 + f2
#         f1 = f2
#         f2 = formula
#         looping += 1
#     return f2
# print(fibonacci_iterative())
#
#
# # Book solution
# def fibonacci_iterative(n=int(input())):
#     previous = 0
#     current = 1
#     for i in range(1,n):
#         current_old = current
#         current = previous + current
#         previous = current_old
#     return current
# print(fibonacci_iterative())


# My solution
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
