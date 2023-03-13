hit = higher = smaller = total = 0
students = 1
print('ALTERNATIVAS (A) (B) (C) (D) (E)')
while True:
    for c in range(1, 10 + 1):
        question = str(input(f'Digite a reposta da questão {c}: ')).upper()
        if c == 1 and question == 'A':
            hit += 1
        if c == 2 and question == 'B':
            hit += 1
        if c == 3 and question == 'C':
            hit += 1
        if c == 4 and question == 'D':
            hit += 1
        if c == 5 and question == 'E':
            hit += 1
        if c == 6 and question == 'E':
            hit += 1
        if c == 7 and question == 'D':
            hit += 1
        if c == 8 and question == 'C':
            hit += 1
        if c == 9 and question == 'B':
            hit += 1
        if c == 10 and question == 'A':
            hit += 1
    print(f'No total você acertou {hit} questões!')
    total += hit
    if students == 1:
        higehr = hit
        smaller = hit
    else:
        if hit > higher:
            higher = hit
        if hit < smaller:
            smaller = hit
    more = str(input('Registrar mais notas?[S/N] ')).lower()
    if more == 'n':
        break
    else:
        hit = 0
        students += 1
total_hit = total / students
if students < 2:
    print('Apenas um estudante foi registrado, então apenas a nota dele é a mais alto e mais baixa')
else:
    print(f'O aluno que tirou a maior nota acertou {higher} questões')
    print(f'O aluno que tirou a menor nota acertou {smaller} questões')
print(f'O total de alunos registrados é {students}')
print(f'A média da turma é {total_hit:.1f}')
