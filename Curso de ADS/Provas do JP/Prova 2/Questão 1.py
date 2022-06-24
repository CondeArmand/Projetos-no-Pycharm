# Head
names = []
surnames = []
qtde = int(input("Quantos nomes deseja informar? "))
# Main
for c in range(qtde):
    nome = str(input('Informe nome e sobrenome respectivamente: ')).split(' ')
    names.append(nome[0])
    surnames.append(nome[1])
names.sort()
surnames.sort()
# Showing Result
print('==' * 30)
for k, v in enumerate(names):
    print(f'{v} {surnames[k]}')
