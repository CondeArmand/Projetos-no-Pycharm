from time import sleep
vel = float(input('Qual a velocidade atual do carro? '))
print('Processando...')
sleep(2)
if vel > 80:
    exc = vel - 80
    mult = exc * 7
    print('Você foi multado por exceder {}Km/h do limite de velocidade!.'.format(exc))
    print('Sua multa é de R${}!'.format(mult))
else:
    print('Muito bem, você está dentro do limite de velocidade!')
print('Tenha um otimo dia! Dirija com segurança!')
