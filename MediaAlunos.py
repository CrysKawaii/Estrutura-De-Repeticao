classes = int(input('Digite a quantidade de turmas: '))
average = 0
count = 1
while count <= classes:
    students = int(input(f'Digite a quantidade de alunos da {count}ª turma: '))
    if students > 40:
        print('As turmas não podem ter mais de 40 alunos!')
        continue
    average += students
    count += 1
average = int(average / classes)
print(f'A média de alunos por turma é {average}')
