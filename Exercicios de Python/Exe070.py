nome = []
preco = []
print('-' * 30)
print(' {:^27} '.format('LOJA SUPER BARATÃO'))
print('-' * 30)
sn = 'S'
count = 0
while sn == 'S':
    nome.append(input('Nome do Produto: ').capitalize().strip())
    preco.append(float(input('Preço: R$ ')))
    if preco[-1] >= 1000:
        count += 1
    sn = input('Quer continuar? [S/N] ').upper().strip()[0]
print('-' * 7, 'FIM DO PROGRAMA', '-' * 7)
print(f'O total da compra foi de R${sum(preco):.2f}')
print(f'Temos {count} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a(o) {nome[preco.index(min(preco))]} que custou R${min(preco):.2f}')
