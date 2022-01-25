# Page 38 ... Logical Operators !!!
# Skip 42 "Comparing Strings"
# Page 44 ... Exercise 16 !!!
# Page 48 - 50 ... Loops !!!
# ---------------------------------

# Exercise 16 Improve it!
# ---------------------------------
age = int(input("Enter your age: "))
# if age greater than or equal to 18 and less than 21 print some privileges.
if 18 <= age < 21:
    print(f"{age} y.o. At least you can vote.")
    print(f"{age} y.o. Poker will have to wait.")
# if age greater than or equal to 18 and again greater than or equal to 21 print
# some privileges.
elif age >= 18 and age >= 21:
    print(f"{age} y.o. At least you can vote.")
    print(f"{age} y.o. What are you waiting for? Let's play poker now!")
else:
    print("You are small.")


# Task 1
# ---------------------------------
while True:
    sex = input('Male or Female (M/F): ').upper()
    age = int(input('Write your age: '))
    if sex == "F":
        print('you are NOT Male in age 15 - 20')
    elif sex == 'M' and 15 <= age <= 20:
        print('you are Male in age 15 - 20')
        break
    else:
        print('you are NOT Male in age 15 - 20')

'''
Run example Task 1 until you get correct input and it will be printed 'you are 
Male in age 15 - 20'

------------------------------- 
Male of Female (M/F) ? M
Write your age:80
you are NOT Male in age 15 - 20 
------------------------------- 
Male of Female (M/F) ? M
Write your age:10
you are NOT Male in age 15 - 20 
------------------------------- 
Male of Female (M/F) ? M
Write your age:18
you are Male in age 15 - 20 
------------------------------- 
Process finished with exit code 0
'''


# Example from Milan.
# ---------------------------------
age = 18
sex = 'M'

print( bool(
    sex.lower() == "m"  and  age >= 20
))
