# Exercise 50: Recursive Countdown
# ------------------------------------------------------------------------------



# In this exercise, you will create a countdown function that recursively counts down from
# integer n until we hit 0:

def countdown(n):
    if n == 0:
        print('liftoff!')
    else:
        print(n)
        return countdown(n - 1)


countdown(3)
