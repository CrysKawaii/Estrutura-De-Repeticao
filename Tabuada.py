num = int(input('Digite um número para a tabuada: '))
print(f'Tabuada de {num}')
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
    