# Head
from random import randint
from time import sleep
from Utilidades import linha
vmx = cmx = 0
# Data gathering and Error check loop
while True:
    try:
        vmx = int(input('Velocidade máxima do navio[Km]: '))
    except ValueError:
        print('\033[4;31mERRO! Informe um valor inteiro valido!\033[m')
        continue
    else:
        break
while True:
    try:
        while True:
            cmx = float(input('Carga máxima do navio [1000 t a 3000 t]: '))
            if cmx < 1000 or cmx > 3000:
                print('\033[4;31mERRO! Informe um peso entre 1000 t a 3000 t\033[m')
                continue
            else:
                break
    except ValueError:
        print('\033[4;31mERRO! Informe um valor real valido!\033[m')
        continue
    else:
        break
linha()
print('Calculando...')
sleep(1.5)
# Main Process
nav = (vmx, cmx)
conts = list()
while len(conts) < 50:
    if sum(conts) <= cmx:
        conteiner = randint(1, 100)
        conts.append(conteiner)
    else:
        break
if sum(conts) > cmx:
    conts.pop()
v_20 = vmx - (vmx * 0.20)
v_atual = vmx - (sum(conts) * 0.01)
# Second Process
linha()
print(f"""Quantidade atual de conteiners: {len(conts)}
Peso total atual: {sum(conts)}""")
print(f"""A velocidade atual do navio é de: {v_atual:.2f}Km/h
O tempo estimado para a viagem até Recife é de: {5840.85/v_atual:.2f}Hrs""")
linha()
# Third Process (Opcional)
while True:
    if v_atual <= v_20:
        print("""\033[4;31mA velocidade atual está abaixo dos 20% da velocidade máxima do navio, o conteiner mais 
pesado irá ser retirado...\033[m""")
        print('Recalculando...')
        sleep(2)
        linha()
        conts.remove(max(conts))
        v_20 = vmx - (vmx * 0.20)
        v_atual = vmx - (sum(conts) * 0.01)
        print(f"""Quantidade atual de containers: {len(conts)}
Peso total atual: {sum(conts)}""")
        print(f"""A velocidade atual do navio é de: {v_atual:.2f}Km/h
O tempo estimado para a viagem até Recife é de: {5840.85 / v_atual:.2f}Hrs""")
        linha()
    else:
        break
print('<< Programa encerrado! >>')
