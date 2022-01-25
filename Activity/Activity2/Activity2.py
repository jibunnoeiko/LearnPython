# Activity 2: Finding a Solution Using the Pythagorean Theorem in Python
# In this activity, you will determine the Pythagorean distance between three points. You
# will utilize a docstring and comments to clarify the process.
# In this activity, you need to assign numbers to the x, y, and z variables, square the
# variables, and take the square root to obtain the distance, while providing comments
# along the way and a docstring to introduce the sequence of steps. To complete this
# activity, you'll utilize multiple variables, comments, and docstrings to determine the
# Pythagorean distance between three points.
#
# 20 | Vital Python | Math, Strings, Conditionals, and Loops
# The steps are as follows:
# 1. Write a docstring that describes what is going to happen.
# 2. Set x, y, and z as equal to 2, 3, and 4.
# 3. Determine the Pythagorean distance between x, y, and z.
# 4. Include comments to clarify each line of code.
# You should get the following output:
# 5.385164807134504


# Activity 2
# ------------------------------------------------------------------------------
""" Finding a Solution Using the Pythagorean Theorem in Python
    Formula: x**2 + y**2 = z**2 x**2 + y**2 = z**2 """
x, y, z = 2, 3, 4
d = x**2 + y**2 + z**2
print(d**0.5)