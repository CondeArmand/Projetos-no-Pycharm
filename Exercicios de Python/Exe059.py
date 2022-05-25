from time import sleep
A = int(input('Primeiro valor: '))
B = int(input('Segundo valor: '))
AB = [A, B]
opcoes = 0
while opcoes != 5:
    opcoes = int(input('''
[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
>>>>> Qual é a sua opção? '''))
    if opcoes == 1:
        print(f'O resultado de {A} + {B} é {sum(AB)}')
        print('=-' * 20)
    elif opcoes == 2:
        print(f'O resultado entre {A} x {B} é {A * B}')
        print('=-' * 20)
    elif opcoes == 3:
        print(f'Entre {A} e {B} o maior valor é {max(AB)}')
        print('=-' * 20)
    elif opcoes == 4:
        print('Informe os valores novamente')
        A = int(input('Primeiro valor: '))
        B = int(input('Segundo valor: '))
        AB = [A, B]
    elif opcoes == 5:
        print('Terminando...')
        sleep(1)
print('Programa encerrado. Volte sempre!')
