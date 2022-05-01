num = int(input())
n1 = 1
n2 = 0
for c in range(0, num - 1):
    print(n2, end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print(n2)
