words = ['aaa','bbb','aaa']
w = words.split
for word in words:
    print(word)

count_word = {}
new_word = 'abc'

# count_word[w] = 1
if new_word in count_word:
    print(f"abc is in dict and it value is \n{count_word[new_word]}")
else:
    count_word[new_word] = 1
    print('abc not in dict')

print(count_word)
