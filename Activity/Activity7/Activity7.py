# Activity 7
# ------------------------------------------------------------------------------


employees = [
    {'name':'Vladislav Henkel','age':19,'department':'programming'},
    {'name':'Milan Brzon','age': 50,'department':'programming'},
    {'name':'Sujan Patel','age':33,'department':'HR'}
]
print(employees)


for e in employees:
    print('Name:',e['name'],
          '\nAge:',e['age'],
          '\nDepartment:',e['department'],
          '\n-----------------------------')

# My solution
for e in employees[2:]:
    print('Name:',e['name'],
          '\nAge:',e['age'],
          '\nDepartment:',e['department'],
          '\n-----------------------------')

# Solution in book
for e in employees:
    if e['name'] == 'Sujan Patel':
        print('Name:',e['name'],
              '\nAge:',e['age'],
              '\nDepartment:',e['department'],
              '\n-----------------------------')
