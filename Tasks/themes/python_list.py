# List exercise
# ------------------------------------------------------------------------------


# 1
def lst_sum(lst):
    counter = 0
    for l in lst:
        counter += l
    print(counter)


lst_sum([1, 2, 3, 4, 5])


# 2
def lst_sum(lst):
    counter = 1
    for l in lst:
        counter *= l
    print(counter)


lst_sum([1, 2, 3, 4, 5])


# 3
def lst_sum(lst):
    count_max = 0
    for l in lst:
        if l > count_max:
            count_max = l
    print(count_max)

lst_sum([1, 2, 45, 3, 4, 5])


# 4
def lst_sum(lst):
    count_min = 0
    for l in lst:
        if l < count_min:
            count_min = l
    print(count_min)

lst_sum([1, 2, 45, 3, -4, 5])