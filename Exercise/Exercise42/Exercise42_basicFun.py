# Exercise 42: Defining and Calling the Function in |Shell|
# ------------------------------------------------------------------------------



# Example!
def add_up(x,y):
    # output: 4
    return x + y
add_up(1,3)

# In a Python shell, enter the function definition. Note that the tab spacing
# needs to match the following output:
def get_second_element(mylist):
    if len(mylist) > 1:
        return mylist[1]
    else:
        return 'List was too small'


get_second_element([1,2,3]) # => 2
get_second_element([1]) # => 'List was too small'

# If you dant wanna use shell, just add print() for call function
print(get_second_element([1,2,3])) # => 2
print(get_second_element([1])) # => 'List was too small'
