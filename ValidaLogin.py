while True:
    name = str(input('Digite se nome de usuário: '))
    password = str(input('Digite sua senha: '))
    if password == name:
        print('Erro! Senha não pode ser igual ao nome de usuário!')
        continue
    else:
        break
