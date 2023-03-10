real = 1
cents = 99
print('LOJA QUASE DE DOIS - TABELA DE PREÇOS')
for c in range(50):
    print(f'{c + 1} - R${real}.{cents}')
    real += 2
    cents -= 1
