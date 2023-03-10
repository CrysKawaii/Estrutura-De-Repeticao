how_many = int(input('Digite quantos número vai querer digitar: '))
higher = smaller = addiction = 0
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
print(f'O menor é {smaller}')
print(f'O maior é {higher}')
print(f'A soma deles é {addiction}')
