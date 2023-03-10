print('Candidato A [1]')
print('Candidato B [2]')
print('Candidato C [3]')
candidate_a = candidate_b = candidate_c = 0
how_many = int(input('Digite o número de eleitores: '))
for c in range(how_many):
    while True:
        vote = int(input('Digite seu voto: '))
        if vote > 3 or vote < 1:
            print('Opção inválida! Digite 1, 2 ou 3 para seu candidato!')
            continue
        else:
            break
    if vote == 1:
        candidate_a += 1
    elif vote == 2:
        candidate_b += 1
    elif vote == 3:
        candidate_c += 1
print(f'O candidato A teve {candidate_a} votos')
print(f'O candidato B teve {candidate_b} votos')
print(f'O candidato C teve {candidate_c} votos')
