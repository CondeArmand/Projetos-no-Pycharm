from time import sleep
print('=' * 8, '\033[4;34mLOJAS GUANABARA\033[m', '=' * 8)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual opção? '))
print('Processando...')
sleep(1)
if opcao == 1:
    print('Ao pagar a vista você ganha 10% de desconto, o valor a ser pago será R$ {}'.format(preco - (preco * 0.10)))
elif opcao == 2:
    print('Ao pagar no cartão a vista, você ganha 5% de desconto, o valor a ser pago será R$ {}'.format(preco - (preco * 0.05)))
elif opcao == 3:
    print('O valor a ser pago será de R$ {}'.format(preco))
elif opcao == 4:
    pqnts = int(input('Quantas parcelas? '))
    print('Processando...')
    sleep(1)
    print('''Ao pagar no cartão em 3x ou mais será cobrado 20% de juros.
Sua compra será parcelada em {}x de R$ {:.2f} com juros.
O valor final da sua compra será de R$ {:.2f}'''.format(pqnts, (preco * 1.20) / pqnts, preco * 1.20))
else:
    print('\033[4;32mErro, insira uma opção válida.')
