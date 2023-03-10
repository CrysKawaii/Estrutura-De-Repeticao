how_many = int(input('Digite quantos CDs comprou: '))
total = 0
for c in range(how_many):
    price = float(input(f'Digite o valor do {c + 1}° CD: R$'))
    total += price
average = total / how_many
print(f'O total gasto foi de R${total:.2f}')
print(f'A média de valor de cada CD é R${average:.2f}')
