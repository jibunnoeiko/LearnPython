# Over The Road

# Example:

# 1_|  |  |_6
# 3_|  |  |_4
# 5_|  |  |_2

# over_the_road(address, n)
# over_the_road(1, 3) = 6
# over_the_road(3, 3) = 4
# over_the_road(2, 3) = 5
# over_the_road(3, 5) = 8

def over_the_road(address, n):
    return 2 * n + 1 - address


result = over_the_road(3,3)
print(result)
