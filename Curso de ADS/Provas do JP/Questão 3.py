# Listas onde serão armazenados os produtos e suas Informações
setor_1 = []
setor_2 = []

on = 'n'             # variavel responsavel por ligar e desligar o programa
while on == 'n':     # While usado para repetir ou não o programa

    # o opcoes será responsavel por mostrar e armazenar a opção escolhida no menu pelo o usuario, para que seja usada...
    # ...no restante do codigo
    opcoes = int(input('''Escolha uma opção: 
1 - Cadastrar produtos;
2 - Informar quantidade de produtos de um determinado setor;
3 - Informar o total do capital investido;
4 - Encerrar programa.
-> '''))
    print('')

    # Conjunto de if's e elif's que irão ser executados de acordo com a opção escolhida pelo usuario no inicio do...
    # ...codigo.
    on1 = 's'
    if opcoes == 1:
        while on1 == 's':
            nome = input('Informe o nome do produto: ')
            setor = int(input('Informe o setor em que o(s) produto(s) será(ão) alocado(s): '))
            qp = map(float, input('Informe a quantidade e preço respectivamente: ').split())
            print('')

            # O primeiro if será responsavel por cadastrar os produtos em um 'setor' determinado pelo usuario. Setores
            # esses que podem ser aumentados ou diminuidos de acordo com o pedido pelo 'cliente', isso sendo feito com
            # uma pequena alteração no codigo para incluir-los

            if setor == 1:
                setor_1.append(nome)
                setor_1.append(setor)
                setor_1.extend(qp)

            # Através das funções de lista, as informações de cada produto é armazenado na lista correspondente ao...
            # ...'setor' escolhido
            elif setor == 2:
                setor_2.append(nome)
                setor_2.append(setor)
                setor_2.extend(qp)

            on1 = input('Deseja adicionar outro? S ou N ? ').lower()
            print('')

    elif opcoes == 2:
        # O segundo elif é responsavel colher as informações dos produtos correspondentes a sua quantidade em
        # determinado setor para averiguar a quantidade total de todos os produtos presentes no 'setor' escolhido
        setor_escolhido = int(input('Informe qual setor: '))
        if setor_escolhido == 1:
            soma = sum(setor_1[2::4])
            print(f'A quantide de produtos armazenados no setor 1 é {soma:.0f}')
            print('')
        # Ainda usando funções de lista, e utlizando de logica posicional nas listas, os dados são colhidos e é feito
        # o calculo, após isso o mesmo é exibido.
        elif setor_escolhido == 2:
            soma = sum(setor_2[2::4])
            print(f'A quantide de produtos armazenados no setor 2 é {soma:.0f}')
            print('')

    elif opcoes == 3:
        # O terceiro Elif também tem uso de logica posicional nas listas para colher os dados corretos e realizar a...
        # ...soma dos mesmos como é pedido na questão.
        soma = sum(setor_1[3::4]) * sum(setor_1[2::4])
        soma2 = sum(setor_2[3::4]) * sum(setor_2[2::4])
        print(f'O capital investido total é de R${soma + soma2:.2f}')
        print('')

    elif opcoes == 4:   # Elif que serve para decidir se o programa irá continuar ou não de acordo com a decição do...
        # ...usuario
        on = input('Encerrar programa? S ou N ? ').lower()
        print('')
