while True:
    grade = float(input('Digite uma nota entre 0 e 10: '))
    if 0 <= grade <= 10:
        print(f'Nota informada {grade}')
        break
    else:
        print('Nota inválida!')
