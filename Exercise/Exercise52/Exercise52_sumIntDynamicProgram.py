# Exercise 52: Summing Integers
# ------------------------------------------------------------------------------



stored_results = {}

def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print(f'Stopping sum at {i+1} because we have previously computed '
                  f'it')
            result += stored_results[i+1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    return result

print(sum_to_n(5))
print(sum_to_n(6))
