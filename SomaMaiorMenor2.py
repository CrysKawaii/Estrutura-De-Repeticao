higher = smaller = addiction = 0
while True:
    how_many = int(input('Digite quantos número quer digitar(entre 0 e 1000): '))
    if how_many > 1000 or how_many < 0:
        continue
    else:
        for c in range(how_many):
            num = int(input(f'Digite o {c + 1}° número: '))
            addiction += num
            if c == 0:
                higher = num
                smaller = num
            else:
                if num > higher:
                    higher = num
                if num < smaller:
                    smaller = num
        break
print(f'O menor número é {smaller}')
print(f'O maior número é {higher}')
print(f'A soma desses números é {addiction}')
