on = 'Y'
while on == 'Y':
    while True:
        login = input('Login: ')
        senha = input('Senha: ')
        if login != senha:
            print('Cadastro efetuado com sucesso')
            break
        else:
            print('Erro! Login e senha não podem ser iguais! Digite novamente!')
    on = input('Y ou N')
