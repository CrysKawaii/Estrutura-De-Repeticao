higher = smaller = cod_city_higher = cod_city_smaller = total = total2 = 0
for c in range(5):
    cod = int(input('Qual o código da cidade: '))
    num = int(input('Número de veículos de passeio(em 1999): '))
    total += num
    if num < 2000:
        total2 += num
    accident = int(input('Número de acidente de trânsito com vítimas(em 1999): '))
    if c == 0:
        higher = accident
        smaller = accident
    else:
        if accident > higher:
            cod_city_higher = cod
            higher = accident
        if accident < smaller:
            cod_city_smaller = cod
            smaller = accident
average = total / 5
average2 = total2 / 5
print(f'A cidade com maior índice de acidentes é a {cod_city_higher} com {higher} acidentes')
print(f'A cidade com menor índice de acidentes é a {cod_city_smaller} com {smaller} acidentes')
print(f'A média de veículos nas 5 cidades é {average:.1f}')
print(f'A média de acidentes na cidades com menos de 2000 veículos de passeio é {average2:.1f}')
