# Activity 9: Formatting Customer Names
# -----------------------------------------------------------------------------



def format_customer(first_name, last_name, location=''):

    if location:
        return f'{first_name} {last_name} ({location})'
    else:
        return f'{first_name} {last_name}'


print(format_customer('John', 'Smith', location='California'))
print(format_customer('Mareike', 'Schmidt'))
