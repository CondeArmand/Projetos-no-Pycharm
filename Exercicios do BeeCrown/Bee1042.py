num = map(int, input().split())
n1, n2, n3 = num
if n1 < n2 < n3:
    print('{}\n{}\n{}'.format(n1, n2, n3))
elif n1 < n3 < n2:
    print('{}\n{}\n{}'.format(n1, n3, n2))
elif n2 < n1 < n3:
    print('{}\n{}\n{}'.format(n2, n1, n3))
elif n2 < n3 < n1:
    print('{}\n{}\n{}'.format(n2, n3, n1))
elif n3 < n2 < n1:
    print('{}\n{}\n{}'.format(n3, n2, n1))
elif n3 < n1 < n2:
    print('{}\n{}\n{}'.format(n3, n1, n2))

print('\n{}\n{}\n{}'.format(n1, n2, n3))
