peso = float(input('Insira seu peso em quilogramas (kg): '))
altura = float(input('Insira sua altura em metros (m): '))
imc = peso / (altura ** 2)
print('\033[4;34mSeu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('\033[4;31mCuidado, você está abaixo do peso ideal!')
elif imc <= 25:
    print('\033[4;32mParabêns, você está no peso ideal!')
elif imc <= 30:
    print('\033[4;31mCuidado, você está em sobrepeso!')
elif imc <= 40:
    print('\033[4;31mMuito cuidado! Você está em obesidade!')
else:
    print('\033[4;31mExtremo cuidado! Você está em obesidade mórbida!')
