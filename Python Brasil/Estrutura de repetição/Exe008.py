maior = 0
soma = 0
media = 0
for i in range(0, 5):
    numero = int(input('Informe um numero: '))
    if maior in vars():
        if numero > maior:
            maior = numero
    else:
        maior = numero
    soma = soma + numero
    media = media + numero
print('O maior numero que voce digitou é: {}'.format(maior))
print('A soma de todos os algarismos informados é: {}'.format(soma))
print('A media dos numeros informados é {}'.format(media/5))
