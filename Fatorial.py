num = int(input('Digite um número: '))
print('O fatorial desse número é:')
print(f'{num}! = ', end='')
fat = 1
for c in range(num, 0, -1):
    if c == 1:
        print(c, end=' ')
    else:
        print(c, end='.')
    fat *= c
print('=', end=' ')
print(fat)
