casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe seu salario atual: R$ '))
anos = int(input('Informe quantos anos de financiamento deseja: '))
pres = casa/ (anos * 12)
pres2 = salario * 0.30
if pres <= pres2:
    print('\033[0;32m --Parabéns, seu empréstimo foi aprovado!!! ',end='')
    print('e sua prestação será de R${:.2f}-- \033[0;32m'.format(pres))
else:
    print('\033[0;31m --Infelizmente seu empréstimo foi recusado por não atender as exigencias-- \033[0;31m')
