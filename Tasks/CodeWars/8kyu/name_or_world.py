# Hello, Name or World!

def hello(name):
    if name:
        print(f'Hello, {name.title()}!')
    else:
        print('Hello, World!')

hello(input('Enter: '))

# def hello(name=""):
#     print(f"Hello, {name[0].upper()}{name.lower()[1:]}!" if name else "Hello, "
#                                                                       "World!")
#
# hello(input('Enter: '))
