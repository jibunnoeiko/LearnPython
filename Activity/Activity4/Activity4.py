# Activity 4: Finding the Least Common Multiple (LCM)
# In this activity, you will find the LCM of two divisors. The LCM of two divisors is the first
# number that both divisors can divide.
# For instance, the LCM of 4 and 6 is 12, because 12 is the first number that both 4 and 6
# can divide. You will find the LCM of 2 numbers. You will set the variables, then initialize
# a while loop with an iterator and a Boolean that is True by default. You will set up a
# conditional that will break if the iterator divides both numbers. You will increase the
# iterator and print the results after the loop completes.
# In this activity, using the following steps, you need to find the LCM of 24 and 36.
# The steps are as follows:

# 1. Set a pair of variables as equal to 24 and 36.

# 2. Initialize the while loop, based on a Boolean that is True by default, with an iterator.

# 3. Set up a conditional to check whether the iterator divides both numbers.

# 4. Break the while loop when the LCM is found.

# 5. Increment the iterator at the end of the loop.

# 6. Print the results.

# You should get the following output:
# The Least Common Multiple of 24 and 36 is 72.


# Activity 4
# ------------------------------------------------------------------------------
def lcm(a, b, x):

    while True:
        x += 1
        if not x%a:
            if not x%b:
                print(f'lcm for {a} and {b} is {x}.')
                break


lcm( int(input('First number: ')),  int(input('Second number: ')), 0 )


# continue in home work 3 =>
