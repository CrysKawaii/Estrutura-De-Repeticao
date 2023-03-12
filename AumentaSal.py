wage = float(input('Digite seu salário inicial: R$'))
per = 1.5
increase = 0
for c in range(1995, 2023):
    increase += (wage * per/100)
    wage += increase
    if c >= 1997:
        per *= 2
    print(f'{wage:.2f}')
# ESSE DESAFIO É ANTIGO ENTÃO PRESUMO QUE QUANDO FOI FEITO NÃO DEVE TER ACONTECIDO ESSA CURVA TÃO INSANA NO VALOR
