num = int(input('Digite um número qualquer: '))
div = num % 2
if div == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))