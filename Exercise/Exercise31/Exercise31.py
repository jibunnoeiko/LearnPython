# Exercise 31: Exploring Tuple Properties in Our Shopping Lis
# ------------------------------------------------------------------------------


t = ('bread','milk','eggs')
print(len(t))

# Can't be changed
# t.append('apple','juice','potato')
# t[2] = 'apple'
print(t + ('apple','orange'))
print(t)

t_mixed = 'apple', True, 3
print(t_mixed)

t_shopping = ('apple',3),('orange',3),('apple',3)
print(t_shopping)
