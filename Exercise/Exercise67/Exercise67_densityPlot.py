# Exercise 67 Generating a Density Plot to Visualize the Score of Students
# ------------------------------------------------------------------------------



import seaborn as sns
data = [90, 80, 50, 42, 89, 78, 34, 70, 67, 73, 74, 80, 60, 90, 90]
sns.distplot(data)

import matplotlib.pyplot as plt
plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')
plt.show()
