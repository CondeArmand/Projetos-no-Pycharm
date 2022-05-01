n1 = int(input())
n2 = int(input())
s = 0
for n in range(n1 + 1, n2):
    print(n, end=' ')
    s = s + n
print('\n{}'.format(s))
