# Designer Door Mat
# ------------------------------------------------------------------------------


n, m = map(int, input().split())
pattern = '.|.'

for i in range(1, n, 2):
    print((pattern*i).center(m, '-'))
print('WELCOME'.center(m).replace(' ', '-'))
for i in reversed(range(1, n, 2)):
    print((pattern*i).center(m, '-'))

n, m = map(int, input().split())
pattern = [('.|.'*i).center(m, '-') for i in range(1, n, 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
