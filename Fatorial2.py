fat = 1
while True:
    num = int(input('Digite um número entre 0 e 16: '))
    if num < 0 or num > 16:
        continue
    else:
        print('O fatorial desse número é:')
        print(f'{num}! =', end=' ')
        for c in range(num, 0, -1):
            if c == 1:
                print(c, end=' ')
            else:
                print(c, end='.')
            fat *= c
    print(f'= {fat}')
    proceed = str(input('Deseja refazer? [S/N}'))
    if proceed == 'n':
        break
    else:
        fat = 1
