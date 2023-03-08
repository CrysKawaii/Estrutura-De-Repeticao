while True:
    name = str(input('Digite seu nome de usuário: '))
    if len(name) < 3:
        continue
    while True:
        age = int(input('Digite sua idade: '))
        if 0 < age < 150:
            break
    while True:
        wage = float(input('Digite o valor do seu salário: R$'))
        if wage > 0:
            break
    while True:
        sex = str(input("Digite seu sexo[F/M]: ")).lower()
        if sex in 'fm':
            break
    while True:
        civil_status = str(input('Digite seu estado civil, (s) (c) (d) (v): ')).lower()
        if civil_status in 'scdv':
            break
    break
print('Validação completa!')
