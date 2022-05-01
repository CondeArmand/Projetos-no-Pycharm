linhas = int(input())
for n in range(1, linhas + 1):
    if n % 2 == 0:
        n1 = n
        n2 = n * n
        n3 = n2 * n
        print('{} {} {}'.format(n1, n2, n3))
    else:
        n1 = n
        n2 = n * n
        n3 = n2 * n
        print('{} {} {}'.format(n1, n2, n3))
