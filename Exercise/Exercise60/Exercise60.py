# Exercise 60: Creating and Writing Content to Files to Record the Date and
# Time in a Text File
# ------------------------------------------------------------------------------
'''
Doc:
• R: The default mode. This opens a file for reading.
• W: The write mode. This opens a file for writing, creates a new file if the
file does
not exist, and overwrites the content if the file already exists.
• X: This creates a new file. The operation fails if the file exists.
• A: This opens a file in append mode, and creates a new file if a file does
not exist.
• B: This opens a file in binary mode.
'''



f = open('log.txt', 'w')

from datetime import datetime
import time
for id in range(0, 10):
    print(datetime.now().strftime('Data: %Y-%m-%d Time: %H:%M:%S - '), 'ID: ',id)
    f.write(datetime.now().strftime('Data: %Y-%m-%d Time: %H:%M:%S - '))
    time.sleep(1)
    f.write(f'ID: {str(id)}')
    f.write("\n")
f.close()

x = 2
assert x < 1, "Invalid value"
