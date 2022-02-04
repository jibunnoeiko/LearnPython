# Find the Runner-Up Score
# ------------------------------------------------------------------------------



if __name__ == '__main__':
    n = int(input('Number: '))
    arr = map(int, input('List: ').split())
    print(sorted(set(arr))[-2])