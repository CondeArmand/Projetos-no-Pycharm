setor_1 = []
setor_2 = []
on = 'n'
while on == 'n':
    opcoes = int(input('''Escolha uma opção: 
1 - Cadastrar produtos;
2 - Informar quantidade de produtos de um determinado setor;
3 - Informar o total do capital investido;
4 - Encerrar programa.
-> '''))
    print('')
    if opcoes == 1:
        nome = input('Informe o nome do produto: ')
        setor = int(input('Informe o setor em que o(s) produto(s) será(aõ) alocado(s): '))
        qp = map(float, input('Informe a quantidade e preco respectivamente: ').split())
        print('')

        if setor == 1:
            setor_1.append(nome)
            setor_1.append(setor)
            setor_1.extend(qp)
        elif setor == 2:
            setor_2.append(nome)
            setor_2.append(setor)
            setor_2.extend(qp)

    elif opcoes == 2:
        setor_escolhido = int(input('Informe qual setor: '))
        if setor_escolhido == 1:
            soma = sum(setor_1[2::4])
            print(setor_1[2::4])
            print(f'A quantide de produtos armazenados no setor 1 é {soma:.0f}')
            print('')
        elif setor_escolhido == 2:
            soma = sum(setor_2[2::4])
            print(f'A quantide de produtos armazenados no setor 2 é {soma:.0f}')
            print('')

    elif opcoes == 3:
        soma = sum(setor_1[3::4])
        soma2 = sum(setor_2[3::4])
        print(f'O capital investido total é de R${soma + soma2:.2f}')
        print('')

    elif opcoes == 4:
        on = input('Encerrar programa? S ou N ? ').lower()
        print('')
