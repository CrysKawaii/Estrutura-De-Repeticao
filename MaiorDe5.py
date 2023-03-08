higher = 0
for c in range(5):
    num = int(input('Digite um número: '))
    if c == 0:
        higher = num
    else:
        if higher < num:
            higher = num

print(f'O maior número é {higher}')
