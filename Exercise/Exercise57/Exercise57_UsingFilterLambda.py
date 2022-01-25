# Exercise 57: Using the Filter Lambda
# ------------------------------------------------------------------------------



nums = list(range(50))

# Use a lambda function to filter the values that are divisible by 3 or 7:
filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)
print(list(filtered))


names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
print(sorted(names, key=lambda x: len(x)))
