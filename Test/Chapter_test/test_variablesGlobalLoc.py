x = 2
y = x
x = 4
print('x =', x)
# --------------------


x = 5
def do_things():
    print('Now x =', x)
do_things()

def my_func():
    y = 5
    return 2
print(my_func())
# --------------------


x = 3
def my_func():
    x = 5
    print(x)
my_func()


score = 0
def update_score(new_score):
    score = new_score
update_score(100)
print(score)
# --------------------


# The Global Keyword
score = 0
def update_score(new_score):
    global score
    score = new_score
update_score(100)
print(score)
# --------------------


# The Nonlocal Keyword
x = 4
def my_func():
    x = 3
    def inner():
        nonlocal x
        print(x)
    inner()
my_func()
# --------------------


# Lambda Functions
# Ex/ lambda arguments : expression
def add_up(x,y):
    return x + y
print(add_up(2,5)) # => 7


add_up = lambda x, y: x + y
print(add_up(2,5)) # => 7
# --------------------


# Mapping with Lambda Functions
names = ['Magda', 'Jose', 'Anne']

# without map()
lenghts = []
for name in names:
    lenghts.append(len(name))
print(lenghts)

# with map()
lenghts = list(map(len, names))
print(lenghts)

print(sum(lenghts) / len(lenghts))
# --------------------



# Filtering with Lambda Functions
names = ['Karen', 'Jim', 'Kim']
print(list(filter(lambda name: len(name) == 3, names)))
# --------------------



# Sorting with Lambda Functions
names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
sorted(names, key=lambda x: len(x))
# --------------------
