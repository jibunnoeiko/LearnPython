# Activity 5: Building Conversational Bots Using Python
# ------------------------------------------------------------------------------

print('Whats you name?')
name = input()
print(f'Hi {name}. Nice to meet you!')

print('How level are you? 0 is very low-lvl. And 10 is a high-lvl')
lvl = input()
lvl = int(lvl)

if lvl >= 5:
    print(f'{name}, awesome work dude!')
    print('How much time you play?')

    days = input()
    days = int(days)

    print(f'{name}, you\'ve been playing for so long, the whole {days} days')

elif lvl <= 5:
    print('Don\'t worry, I can help you! :D')
    print('You are okay?')

    mood = input().lower()

    if mood == 'no':
        print('Oh no man, sorry. But I really can help you, improve you lvl! :D')
    else:
        print('Okay dude, you awesome! :D')

print('Thx for talking with me, see you later, bye! :D')
