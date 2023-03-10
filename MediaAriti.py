num = int(input('Quantas notas vai digitar: '))
addiction = 0
for c in range(1, num + 1):
    grade = float(input(f'Digite a {c}° nota: '))
    addiction += grade
average = addiction / num
print(average)
