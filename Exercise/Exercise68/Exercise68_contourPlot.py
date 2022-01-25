# Exercise 68 Creating a Contour Plot
# ------------------------------------------------------------------------------



# Initialize the weight recording data using the following code in a new cell:
weight = [85.08,79.25,85.38,82.64,80.51,77.48,79.25,78.75,77.21,73.11,82.03,
          82.54,74.62,79.82,79.78,77.94,83.43,73.71,80.23,78.27,78.25,80.00,
          76.21,86.65,78.22,78.51,79.60,83.88,77.68,78.92,79.06,85.30,82.41,
          79.70,80.16,81.11,79.58,77.42,75.82,74.09,78.31,83.17,75.20,76.14]

import seaborn as sns
sns.kdeplot(list(range(0,44)), weight, kind='kde', cmap='Reds', )

# Add legend, title, and axis labels to the plot:
import matplotlib.pyplot as plt
plt.legend(labels=['a','b'])
plt.title('Weight Dataset - Contour Plot')
plt.ylabel('height (cm)')
plt.xlabel('width (cm)')
plt.show()
