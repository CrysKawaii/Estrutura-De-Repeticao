higher = smaller = average = 0
count = 0
while True:
    temp = float(input('Digite a temperatura: '))
    if count == 0:
        higher = temp
        smaller = temp
    else:
        if temp > higher:
            higher = temp
        if temp < smaller:
            smaller = temp
    count += 1
    average += temp / count
    proceed = str(input('Deseja continuar?[S/N] ')).lower()[0]
    if proceed == 'n':
        break
print(f'A maior temperatura informada foi {higher}')
print(f'A menor temperatura foi {smaller}')
print(f'A média das temperatura informada é {average:.1f}')

