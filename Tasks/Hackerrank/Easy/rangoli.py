# # Rangoli alphabet
# # ------------------------------------------------------------------------------


def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    data = [alphabet[i] for i in range(size)]
    items = list(range(size))
    items = items+items[:-1][::-1]

    for i in items:
        print(i, i+1)
        start = i+1
        original = (data[-start:])
        reverse = original[::-1]
        final = reverse+original[1:]
        final = ('-'.join(final))
        distance = size*4-3
        print(final.center(distance, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
