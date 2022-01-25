# Exercise 54: Helper Currency Conversion
# Helper Functions Exercise in (Test -> test_helpFun.py)
# ------------------------------------------------------------------------------



def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += amount_in_aud * 0.78
    total += amount_in_gbp * 1.29
    return total


print(compute_usd_total(amount_in_gbp=10))


# Create a currency conversion function with an optional margin:
def convert_currency(amount, rate, margin=0):
    return amount * rate * (1 + margin)
def compute_usd_total(amount_in_aud=0, amount_in_gbp=0):
    total = 0
    total += convert_currency(amount_in_aud, 0.78)
    total += convert_currency(amount_in_gbp, 1.29, 0.01)
    return total


print(compute_usd_total(amount_in_gbp=10))
