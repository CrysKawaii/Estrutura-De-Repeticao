interval = interval2 = interval3 = interval4 = 0
while True:
    num = int(input('Digite um número entre 0 e 100(negativo para sair): '))
    if num < 0:
        break
    if 0 < num < 25:
        interval += 1
    elif 26 < num < 50:
        interval2 += 1
    elif 51 < num < 75:
        interval3 += 1
    elif 76 < num < 100:
        interval4 += 1
print(f'{interval} estão entre 0 e 25')
print(f'{interval2} estão entre 26 e 50')
print(f'{interval3} estão entre 51 e 75')
print(f'{interval4} estão entre 76 e 100')
