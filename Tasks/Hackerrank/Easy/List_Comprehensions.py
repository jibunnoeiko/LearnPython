# List Comprehensions
# ------------------------------------------------------------------------------


if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)
           if (i+j+k) != n])


if __name__ == '__main__':
    x, y, z, n = int(input()), int(input()), int(input()), int(input())

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    print([i,j,k])
