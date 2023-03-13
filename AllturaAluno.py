higher = smaller = num_higher = num_smaller = 0
for c in range(10):
    num = int(input('Digite o número do aluno: '))
    height = int(input('Digite a altura do aluno(em cm): '))
    if c == 0:
        higher = height
        smaller = height
    else:
        if height > higher:
            num_higher = num
            higher = height
        if height < smaller:
            num_smaller = num
            smaller = height
print(f'O número do aluno mais alto é {num_higher} com {higher}cm de altura')
print(f'O número do aluno mais baixo é {num_smaller} com {smaller}cm de altura')
