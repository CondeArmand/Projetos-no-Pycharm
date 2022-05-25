pesos = []
for c in range(5):
    pesos.append(float(input(f'Insira o peso da {c + 1}ª pessoa: ')))
print(f'O maior peso lido foi de {max(pesos)}Kg')
print(f'O menor peso lido foi de {min(pesos)}Kg')
