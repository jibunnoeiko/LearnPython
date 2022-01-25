# Exercise 49: Exiting the Function During the for Loop
# ------------------------------------------------------------------------------



def is_prime(x):
    for i in range(2,x):
        if  (x%i)==0:
            return (False)
        return True


is_prime(6)
