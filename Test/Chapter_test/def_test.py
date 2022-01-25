total = 0
def num(n):
    global total
    total += n
    print(f'{n} - {total}')


num(2)   #-> New number: {2}
         #-> Total sum: {2}

num(6)   #-> New number: {6}
         #-> Total sum: {8}

num(4)   #-> New number: {4}
         #-> Total sum: {12}
