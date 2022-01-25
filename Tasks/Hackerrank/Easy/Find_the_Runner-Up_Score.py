# Find the Runner-Up Score
# ------------------------------------------------------------------------------



# if __name__ == '__main__':
#     n = int(input('Number: '))
#     arr = map(int, input('List: ').split())
#     print(sorted(set(arr))[-2])
#
#
# if __name__ == '__main__':
#     n = int(input())
#     L = list(map(int, input().split()))
#     a = max(L)
#     L.sort(reverse = True)
#     for i in L :
#         if i < a :
#             print(i)
#             break

if __name__ == '__main__':
    n = int(input())
    lst = map(int, input().split())
    print(sorted(set(lst))[-2])
