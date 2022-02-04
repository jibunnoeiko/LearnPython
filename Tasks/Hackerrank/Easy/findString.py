# find string
# ------------------------------------------------------------------------------



def count_substring(string, sub_string):
    start = string.find(sub_string)
    count = 0
    
    for i in range(start, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


def count_substring(string, sub_string):
    count = []
    length = len(string)
    index = 0
    while length:
        i = string.find(sub_string, index)
        if i == -1:
            return (len(count))
        count.append(i)
        index = i + 1
    return len(count)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
