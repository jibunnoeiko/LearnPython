'''
Task 3.1
Hint:
print('-- start --')
sentence = 'My name is Milan STOP Brzon'
words = sentence.split(' ')
print('-- end --')

Create function:
	printWords(sentence)
	-->  My      1) Print everything ... all words
-->  name
-->  is
-->  Milan
-->  STOP    2) Don't print any more if there is STOP
-->  Brzon

3) Print only words with capital letter
-->  My
-->  Milan
'''

def myWords(sentence, stopWord):

    print('-- start --')
    sentence = sentence.split(' ')
    for s in sentence:
        if s == s.capitalize():
            print(s)
        elif stopWord == s:
            break
    print('-- end --')


myWords('My name is Milan stop Brzon', input('Stop: '))
