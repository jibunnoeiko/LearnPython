# Exercise 23
# ------------------------------------------------------------------------------

X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Y = [[10,11,12],
     [13,14,15],
     [16,17,18]]

# Initialize a result placeholder
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

# Iterate through rows
for row in range(len(X)):
    # Iterate through columns
    for column in range(len(Y)):
        result[row][column] = X[row][column] + Y[row][column]

print(result)

