nums = ('zero', 'um', 'dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
sn = 's'
while sn == 's':
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {nums[num]}')
    sn = input('Deseja continuar? [S/N] ').lower().strip()[0]
