# Lists
# ------------------------------------------------------------------------------



if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        s = input().split(' ')
        if s[0]=='insert':
            lst.insert(int(s[1]),int(s[2]))
        if s[0]=='print':
            print(lst)
        if s[0]=='remove':
            lst.remove(int(s[1]))
        if s[0]=='append':
            lst.append(int(s[1]))
        if s[0]=='sort':
            lst.sort()
        if s[0]=='pop':
            lst.pop()
        if s[0]=='reverse':
            lst.reverse()

# Output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
