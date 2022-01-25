# Write a function
# ------------------------------------------------------------------------------



def is_leap(year):
    leap = False
    bad_year = [1800, 1900, 2100, 2200, 2300, 2500]

    if year //4 and year//400:
        if year != bad_year:
            return True
        else:
            return False
    else:
        return leap


year = int(input())
print(is_leap(year))
