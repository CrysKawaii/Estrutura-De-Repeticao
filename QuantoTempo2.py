country1 = int(input('Digite qual a população do país 1: '))
country2 = int(input('Digite qual a população do país 2: '))
growth_rate1 = float(input('Digite a taxa de crescimento do país 1: '))
growth_rate2 = float(input('Digite a taxa de crescimento do país 2: '))
years = 0
while True:
    years += 1
    print(f'População do país 1 no ano {years}: {int(country1)}')
    print(f'População do país 2 no ano {years}: {int(country2)}')
    country1 += (country1 * growth_rate1/100)
    country2 += (country2 * growth_rate2 / 100)
    if country1 >= country2:
        print(f'Foram necessários {years} anos')
        proceed = str(input('Deseja atualizar os dados?[S/N]: '))
        if proceed == 'n':
            break
        else:
            country1 = int(input('Digite qual a população do país 1: '))
            country2 = int(input('Digite qual a população do país 2: '))
            growth_rate1 = float(input('Digite a taxa de crescimento do país 1: '))
            growth_rate2 = float(input('Digite a taxa de crescimento do país 2: '))
            years = 0
print('Programa encerrado!')
