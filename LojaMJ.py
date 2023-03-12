print('LOJAS TABAJARA')
count = 1
total = 0
while True:
    while True:
        price = float(input(f'Digite o valor do produto {count}: R$'))
        if price == 0:
            break
        total += price
        count += 1

    money = float(input('Digite o valor do dinheiro: R$'))
    change = money - total
    print(f'Total: R${total:.2f}')
    print(f'Dinheiro: R${money:.2f}')
    print(f'Troco: R${change:.2f}')
    count = 1
    continue
