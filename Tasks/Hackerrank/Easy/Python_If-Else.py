# Python If-Else
# ------------------------------------------------------------------------------



if __name__ == '__main__':
    n = int(input().strip())

    if (n%2):
        print('Weird')
    elif (n>=21 and n%2 == 0):
        print('Not Weird')
    elif (2<n<5):
        print('Not Weird')
    elif (6<n<20):
        print('Weird')
    else:
        print('Weird')
