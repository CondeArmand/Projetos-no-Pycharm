maior = 0
for i in range(0, 5):
    numero = int(input('Informe um numero: '))
    if maior in vars():
        if numero > maior:
            maior = numero
    else:
        maior = numero

print('O maior numero que voce digitou é: {}'.format(maior))
