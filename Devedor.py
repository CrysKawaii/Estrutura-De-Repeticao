debt = float(input('Digite o valor da dívida: R$'))
fees = 10
portion = 3
print(f'''Valor da dívida     Valor dos juros     Quantidade de parcelas     Valor da parcela
\t{debt}                 0                     1                       {debt}''')
for c in range(4):
    print(f'''
\t{debt + (debt * fees/100)}                 {(debt * fees/100)}                 {portion}                       {(debt + (debt * fees/100)) /portion:.2f}''')
    fees += 5
    portion += 3
