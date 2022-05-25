nomes = []
nomesH = []
idades = []
idadesH = []
idadesM = []
Mmenores20 = 0
sexos = []
for c in range(4):
    print('-' * 5, f'{c + 1}ª PESSOA', '-' * 5)
    nomes.append(input('Nome: ').strip().capitalize())
    idades.append(int(input('Idade: ')))
    sexos.append(input('Sexo [M/F]: ').upper().strip())
    if sexos[-1] == 'M':
        nomesH.append(nomes[-1])
        idadesH.append(idades[-1])
    else:
        idadesM.append(idades[-1])
        if idadesM[-1] < 20:
            Mmenores20 += 1
print(f'A média de idade do grupo é de {sum(idades) / len(idades)}')
print(f'O homem mais velho tem {max(idadesH)} e se chama {nomesH[idadesH.index(max(idadesH))]}')
print(f'Ao todo são {Mmenores20} mulheres com menos de 20 anos')
