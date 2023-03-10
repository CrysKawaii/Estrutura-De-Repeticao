num = int(input('Digite o número de pessoas: '))
addiction = 0
for c in range(1, num + 1):
    age = int(input(f'Digite a idade da {c}° pessoa: '))
    addiction += age
average = addiction / num
print(f'A média de idades dessa turma é {average:.1f}')
if 0 < average < 25:
    print('A turma é jovem!')
elif 26 < average < 60:
    print('A turma é adulta!')
elif average > 60:
    print('A turma é idosa!')
