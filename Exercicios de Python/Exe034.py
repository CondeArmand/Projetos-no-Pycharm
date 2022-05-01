sal = float(input('Informe seu salario: '))
if sal > 1250:
    print('Seu novo salario com um aumento de 10% irá ser: R${:.2f}'.format(sal * 1.10))
else:
    print('Seu novo salario com aumento de 15% irá ser: R${:.2f}'.format(sal * 1.15))
