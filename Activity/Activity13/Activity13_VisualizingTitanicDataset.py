# Activity 13 Visualizing the Titanic Dataset Using a Pie Chart and Bar Plots
# ------------------------------------------------------------------------------



import csv
lines = []
with open('titanic_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        lines.append(line)

data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    p = {}
    for i in range(0, len(headers)):
        p[headers[i]] = d[i]
    passengers.append(p)

survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]

import matplotlib.pyplot as plt
from collections import Counter

# Pie plot
plt.title('Survived')
plt.pie(Counter(survived).values(), labels=['Female','Male'], autopct='%1.1f%%',
        colors=['lightblue', 'lightgreen'])
plt.show()



# Bar plot
plt.title('Survived')
plt.bar(Counter(gender_survived).keys(), Counter(gender_survived).values(),
        color=['lightblue', 'lightgreen'])
plt.show()
