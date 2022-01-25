"""
Python script that tells you the current time
"""

# Activity 8: What's the Time?
# ------------------------------------------------------------------------------



from datetime import datetime

time = datetime.now().time()
if __name__ == '__main__':
    print(time)
