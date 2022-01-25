# Reverse an array of integers
# ------------------------------------------------------------------------------



def reverseArray(a):
    first_num = 0
    last_num = len(a)-1
    while first_num<=last_num:
        a[first_num],a[last_num] = a[last_num],a[first_num]
        first_num += 1
        last_num -= 1
    return a
print(reverseArray([1,2,5,7,9,3,2,86]))


# user from StackOverFlow.com
def reverse(data_list):
    length = len(data_list)
    s = length

    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return new_list
print(reverse([1,4,3,2]))
