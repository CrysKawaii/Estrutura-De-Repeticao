while True:
    num = int(input('Montar a tabuada do número: '))
    start = int(input('Começar por: '))
    end = int(input('Terminar em: '))
    if end < start:
        print('Erro! O final não pode ser menor que o começo! Tente novamente!')
        continue
    else:
        break
for c in range(start, end + 1):
    print(f'{num} x {c} = {num * c}')
