# Exercise 40: Linear Search in Python
# ------------------------------------------------------------------------------



# Start with the list of numbers
l = [5,8,1,3,2]

# Specify a value to search_for
search_for = 0

# Create a result variable that has a default value of -1
result = -1

# Loop through the list. If the value equals the search value,
# set the result, and exit the loop
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break

# Check the result
print(result) # => 1

