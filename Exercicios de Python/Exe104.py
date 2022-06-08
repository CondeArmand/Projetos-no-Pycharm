def leiaint(n=''):
    while True:
        num = input(n)
        if num.isdigit():
            return num
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')