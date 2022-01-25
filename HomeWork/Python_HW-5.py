# Task 4

# Start with an empty shopping list.
# Then repeatedly do input operation:
# A: Apple .... it means add Apple to the list
# 	D: Apple .... it means delete Apple from the list
# 	I: Apple ....          print index of Apple item in the list
# 	P:                      print content of the list
# 	C:       .... clear all items from the list and start from empty list again
# 	E:        .... end of input


lst = []

while True:
        print('What do you want to do?')
        print(' A: Add item\n D: Delete item\n I: Index item\n P: Print content\n '
              'C: Clear all\n E: End of input\n INSERT: Insert item')
        user = input("Enter here: ")
        if user == 'A':
            A = lst.append(int(input('Add item: ')).split())
            print('Item added')
            print(lst)
        elif user == 'D':
            try:
                D = lst.remove(int(input('Delete item: ')))
                print('Item deleted')
                print(lst)
            except:
                print('Let\'s continue')
        elif user == 'Index':
            try:
                I = lst.index(int(input('Index item: ')))
                print(f'I index is - {I}')
            except:
                print('Let\' continue')
        elif user == 'P':
            P = print(lst)
            print(f'Shopping content - {P}')
        elif user == 'C':
            C = lst.clear()
            print(f'List clear')
            print(lst)
        elif user == 'Insert':
            INSERT = lst.insert(int(input('index: ')), input('item: '))
        else:
            print('This command not exist')
