desconto = 0
juros = 0
on = 'S'
while on == 'S':  # Interruptor para repertir ou não a operação.
    # entrada de dados
    compra = int(input('Informe o valor da sua compra: R$ '))

    # nesta parte será definido o metodo de pagamento através das estruturas de decição e repetição...
    # ...Caso seja informado um valor invalido, o programa irá repetir até que seja informado um valor...
    # valido.
    while True:
        pagamento = int(input('''Informe um metodo de pagamento:
[1] À vista
[2] Cartão de Crédito
[3] Parcelado no Boleto
-> '''))
        if pagamento == 1:
            desconto = compra - (compra * 0.15)
            break
        elif pagamento == 2:
            desconto = compra - (compra * 0.05)
            break

    # No terceiro elif, utilizando de estruturas de decição dentro de outra elif. É escolhido o quantidade de...
    # ...parcelamentos e feito o calculo de acordo.

        elif pagamento == 3:
            print('''O parcelamento pode ser de até 12x.
De 2 a 6 parcelas irá ser cobrado 15% além do valor da compra.
De 7 a 12 parcelas irá ser cobrado 30% além do valor da compra.''')

            while True:
                parcelas = int(input('Infome o número de parcelas desejadas: '))
                if 6 >= parcelas > 1:
                    juros = compra * 1.15
                    break
                elif 6 < parcelas <= 12:
                    juros = compra * 1.30
                    break
                else:
                    print('\033[2;32mQuantidade de parcelas invalida!', '\n')
            break
        else:
            print('\033[2;31mEscolha invalida!\033[m', '\n')

    # Nesta etapa será printado o resultado de acordo com o metodo de pagamento escolhido anteriormente.

    print(' ')
    if pagamento == 1 or pagamento == 2:
        print(f'\033[3;32mO valor final da sua compra é R${desconto:.2f}')
    elif pagamento == 3:
        print(f'\033[2;33mO valor final da sua compra é R${juros:.2f}')

    on = input('\033[3;34mDeseja repetir a operação? S ou N ?: \033[m').upper()  # Interruptor para repertir ou
    # não a  operação.
    print('')
