# ---------------------------------------------
# Task 1:
# 1) send to function only 2 params ✅
# 2) initialize x in function by max ✅
# 3) rewrite if to one line ✅

# ---------------------------------------------
def lcm(a, b):
    x = max(a, b)
    while True:
        x += 1
        if not x % v and not x % b:
            print(f'lcm for {a} and {b} is {x}.')
            break


lcm(int(input('First number: ')), int(input('Second number: ')))


# 1.Task: change the code that only result will be printed ✅
# 2.Task: create function that takes two parameters and print result ✅
# 3.Task: Try   x+=1  x+=5  x*=3   ... see page 14, 48
# ---------------------------------------------

# # Task 2:
def before(sentence, character):
    inx = [sentence.index(character)]
    return sentence[:inx]

print('start of program')
result = before('Saa bb cc. Dd ee ff', 'D')
print(result)
# # --> 'Aaa bb cc. '
