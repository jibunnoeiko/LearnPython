# Exercise 65 Creating a Pie Chart to Visualize the Number of Votes in a School
# ------------------------------------------------------------------------------



# Plotting
labels = ['Monica', 'Adrian', 'Jared']
num = [230, 100, 98] # Note: that this does not need to be percentages

import matplotlib.pyplot as plt
plt.title('Voting Results: Club President', fontdict={'fontsize': 20})
plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue',
                                                       'lightgreen',
                                                       'yellow'])
plt.show()
