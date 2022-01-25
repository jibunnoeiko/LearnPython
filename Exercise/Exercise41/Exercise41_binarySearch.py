# Exercise 41: Binary Search in Python
# ------------------------------------------------------------------------------



# Start with a list of numbers
l = [2, 3, 5, 8, 11, 12, 18]


# Specify the value to search_for
search_for = 11


# Create two variables that will represent the start and end locations of the
# sublist you are interested in. Initially, it will represent the start and end
# indices for the entire list
slice_start = 0
slice_end = len(l) - 1


# Add a variable to indicate whether the search was successful
found = False


# Find the midpoint of the list, and check whether the value is greater or
# less than the search term. Depending on the outcome of the comparison, either
# finish the search or update the locations for the start/end of the sublist
while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if l[location] == search_for:
        found = True
    else:
        if search_for < l[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1

# Check results
print(found) # => True
print(location) # => 4
