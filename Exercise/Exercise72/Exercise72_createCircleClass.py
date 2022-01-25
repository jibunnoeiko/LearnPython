# Exercise 72 Creating a Circle Class
# ------------------------------------------------------------------------------



class Circle():
    is_shape = True

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

first_circle = Circle(2, 'blue')
second_circle = Circle(3, 'red')

print(f'<<First Circle>>\nRadius: {first_circle.radius}\nColor:'
      f' {first_circle.color}\n')
print(f'<<Second Circle>>\nRadius: {second_circle.radius}\nColor:'
      f' {second_circle.color}')
