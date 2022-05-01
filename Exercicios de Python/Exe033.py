print('Qual o Maior e Menor Número?')
pri = float(input('Primeiro número: '))
seg = float(input('Segundo número: '))
ter = float(input('Terceiro número: '))
maior = pri
if seg > maior:
    maior = seg
if ter > maior:
    maior = ter
menor = pri
if seg < menor:
    menor = seg
if ter < menor:
    menor = ter
print('O MAIOR valor é: ', maior)
print('O MENOR valor é:', menor)
