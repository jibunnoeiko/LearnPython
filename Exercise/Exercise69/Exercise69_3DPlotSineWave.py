# Exercise 69 Generating 3D plots to Plot a Sine Wave
# ------------------------------------------------------------------------------



from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
X = np.linspace(0, 10, 50)
Y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(X, Y)
Z = (np.sin(X))

# Setup axis
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# Add title and axes labels
ax.set_title("Demo of 3D Plot", size=13)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()



# Before exercise
# ------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# # Split the figure into 2 subplots
# fig = plt.figure(figsize=(8,4))
# ax1 = fig.add_subplot(121) # 121 means split into 1 row , 2 columns, and put
# # in  1st part.
# ax2 = fig.add_subplot(122) # 122 means split into 1 row , 2 columns, and put
# # in  2nd part.
#
# labels = ['Adrian', 'Monica', 'Jared']
# num = [230, 100, 98]
# ax1.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen',
# 'yellow'])
# ax1.set_title('Pie Chart (Subplot 1)')
#
# # Plot Bar Chart (Subplot 2)
# labels = ['Adrian', 'Monica', 'Jared']
# num = [230, 100, 98]
# plt.bar(labels, num, color=['lightblue', 'lightgreen', 'yellow'])
# ax2.set_title('Bar Chart (Subplot 2)')
# ax2.set_xlabel('Candidate')
# ax2.set_ylabel('Votes')
# fig.suptitle('Voting Results', size=14)
#
# plt.show()
# ------------------------------------------------------------------------------
