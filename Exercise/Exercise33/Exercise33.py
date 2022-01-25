# Exercise 33: Implementing Set Operations
# ------------------------------------------------------------------------------


s5 = {1,2,3,4}
s6 = {3,4,5,6}

# use the | operator or the union method for a union operation:
print(s5 | s6)
print(s5.union(s6))

#  use the & operator or the intersection method for an intersection operation:
print(s5 & s6)
print(s5.intersection(s6))

# use the - operator for the difference method to find the difference between
# two sets:
print(s5 - s6)
print(s5.difference(s6))

# use the <= operator or the issubset method to check if one set is a subset
# of another:
print(s5 <= s6)
print(s5.issubset(s6))

s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))

# Check whether s7 is a formal subset of s8, and check whether a set can be a proper
# subset of itself by entering the following code:
print(s7 < s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9,'\n')

# Now use the >= operator or the issuperset method to check whether one set is the
# superset of another. Try it using the following code in another cell:
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)
