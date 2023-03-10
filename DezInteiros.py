pairs = odd = 0
for c in range(10):
    num = int(input(f'Digite o {c + 1}° número: '))
    if num % 2 == 0:
        pairs += 1
    else:
        odd += 1
print(f'Foram digitado {pairs} número pares e {odd} números ímpares')
