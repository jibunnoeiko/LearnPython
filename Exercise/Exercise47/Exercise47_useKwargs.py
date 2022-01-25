# Exercise 47: Using **kwargs
# ------------------------------------------------------------------------------



# Enter the convert_rub_to_usd function defined in the previous exercise:
def convert_rub_to_usd(amount, rate):
    return amount / rate

# Create a new convert_and_sum_list function that will take a list of amounts, convert
# them to USD, and return the sum:
def convert_and_sum_list(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_rub_to_usd(amount, **kwargs)
    return round(total, 2)


print(convert_and_sum_list([100000,300000], rate=float(input('Rate: '))))


# Best example **kw
def printPetNames(owner=None, **pets):
    if owner == None:
        owner = 'unknown'
    print(f"Owner Name: {owner}")
    for pet,name in pets.items():
        print(f"{pet}: {name}")
printPetNames('Jonathan', dog="Brock", fish=["Larry", "Curly", "Moe"],
              turtle="Shelldon")
