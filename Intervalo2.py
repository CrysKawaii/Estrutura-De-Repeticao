n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
addiction = 0
print('Aqui estão os números que se encontram no intervalo desses valores:')
for c in range(n1 + 1, n2):
    print(c)
    addiction += c
print(f'A soma desses números é {addiction}')
