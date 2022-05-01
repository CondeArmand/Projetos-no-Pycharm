print('\033[0;33m||Comparador de números inteiros||\033[m')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o número {}'. format(num2, num1))
else:
    print('Os números {} e {} são iguais.'.format(num1, num2))
