num = int(input())
print('Tabuada de {}: '.format(num))
for n in range(0, 11):
    print('{} x {} = {}'.format(n, num, num * n))
