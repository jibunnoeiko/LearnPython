# Exercise 24
# ------------------------------------------------------------------------------

X = [[1,2],
     [4,5],
     [7,8]]

Y = [[1,2,3,4],
     [5,6,7,8]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# Iterating by row of X
for row_x in range(len(X)):
    # Iterating by column of Y
    for column_y in range(len(Y[0])):
        # Iterating by rows of Y
        for row_y in range(len(Y)):
            result[row_x][column_y] += X[row_x][row_y] * Y[row_y][column_y]

for r in result:
    print(r)
