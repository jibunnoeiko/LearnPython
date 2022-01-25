# Exercise 16 Improve it!

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
# -----------------------------------------------------------------------------
