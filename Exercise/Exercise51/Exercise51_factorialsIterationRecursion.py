# Exercise 51: Factorials with Iteration and Recursion
# ------------------------------------------------------------------------------



# def factorial_iterative(n=int(input())):
#     result = 1
#     for i in range(n):
#         result *= i + 1
#     return result
#
#
# print(factorial_iterative())


def factorial_recursive(n=int(input())):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
    # return 5 * factorial_recursive(4)
    #     return 4 * factorial_recursive(3)
    #         return 3 * factorial_recursive(2)
    #             return 2 * factorial_recursive(1)
    #                 return 1
print(factorial_recursive())
