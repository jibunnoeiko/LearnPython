def print_the_next_number(start):
    print(start + 1)
    if start >= 9:
        return None
    return print_the_next_number(start + 1)
print_the_next_number(0)
