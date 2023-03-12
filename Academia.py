higher_height = smaller_height = average = count = fat = lean = 0
code_higher = code_smaller = code_fat = code_lean = 0
while True:
    cod = int(input('Digite seu código: '))
    if cod == 0:
        break
    height = float(input('Digite sua altura: '))
    if count == 0:
        higher_height = height
        smaller_height = height
    else:
        if height > higher_height:
            higher_height = height
            code_higher = cod
        if height < smaller_height:
            smaller_height = height
            code_smaller = cod
    weight = float(input('Digite seu peso: '))
    if count == 0:
        fat = weight
        lean = weight
    else:
        if weight > fat:
            fat = weight
            code_fat = cod
        if weight < lean:
            lean = weight
            code_lean = cod
    count += 1
print(f'O cliente mais alto é o do código {code_higher} com {higher_height} de altura')
print(f'O cliente mais baixo é o do código {code_smaller} com {smaller_height} de altura')
print(f'O mais gordo é o do código {code_fat} pesando {fat}')
print(f'O mais magro é o do código {code_lean} pesando {lean}')
