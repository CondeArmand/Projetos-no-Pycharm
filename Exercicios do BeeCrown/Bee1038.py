code = map(int, input().split(' '))
n1, n2 = code
if 1 == n1:
    print('Total: R$ {:.2f}'.format(4.00 * n2))
elif 2 == n1:
    print('Total: R$ {:.2f}'.format(4.50 * n2))
elif 3 == n1:
    print('Total: R$ {:.2f}'.format(5.00 * n2))
elif 4 == n1:
    print('Total: R$ {:.2f}'.format(2.00 * n2))
elif 5 == n1:
    print('Total: R$ {:.2f}'.format(1.50 * n2))
