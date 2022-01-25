# Activity 3: Using the input() Function to Rate Your Day
# In this activity, you need to create an input type where you ask the user
# to rate their day on a scale of 1 to 10.
# Using the input() function, you will prompt a user for input and respond with a
# comment that includes the input. In this activity, you will print a message to
# the user asking for a number. Then, you will assign the number to a variable
# and use that variable in a second message that you display to the user.
# The steps are as follows:
# 1) Open a new Jupyter Notebook.
# 2) Display a question prompting the user to rate their day on a number scale
# of 1 to 10.
# 3) Save the user's input as a variable.
# 4) Display a statement to the user that includes the number.


# Activity 3
# ------------------------------------------------------------------------------
# Rate users day of 1 to 10.
rateDay = int(input("Hello, rate your day of 1 to 10 -> "))
if rateDay <= 4:
    print(f"{rateDay}, sadness ☹")
if 4 < rateDay <= 7:
    print(f"{rateDay}, cool 😃")
if 7 < rateDay <= 10:
    print(f"{rateDay}, awesome 😎")
