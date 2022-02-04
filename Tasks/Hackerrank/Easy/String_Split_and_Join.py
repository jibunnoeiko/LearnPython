# String Split and Join
# ------------------------------------------------------------------------------



def split_and_join(line):
    return '-'.join(line.split(' '))

if __name__ == '__main__':
    line = 'Hello World! How are you?'
    result = split_and_join(line)
    print(result)