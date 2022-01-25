# Activity 6
# ------------------------------------------------------------------------------


employees = [['John Mckee',    38,   'Sales'  ],
             ['Lisa Crawfrod', 29, 'Marketing'],
             ['Sujan Patel',   33,     'HR'   ]]

for e in employees:
    print(f'Name: {e[0]}\n'
          f'Age: {e[1]}\n'
          f'Department: {e[2]}'
          f'\n{"-"*20}')
