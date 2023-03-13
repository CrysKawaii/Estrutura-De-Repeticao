print('''
Especificação   Código   Preço
Cachorro Quente  100     R$ 1,20
Bauru Simples    101     R$ 1,30
Bauru com ovo    102     R$ 1,50
Hambúrguer       103     R$ 1,20
Cheeseburguer    104     R$ 1,30
Refrigerante     105     R$ 1,00
''')
price = item_value = total = 0

while True:
    cod = int(input('Digite o código do item que deseja: '))
    if cod == 100 or cod == 103:
        price = 1.20
    elif cod == 101 or cod == 104:
        price = 1.30
    elif cod == 102:
        price = 1.50
    elif cod == 105:
        price = 1
    quant = int(input('DIgite a quantidade desejada desse item: '))
    item_value = price * quant
    print(f'Você vai pagar R${item_value:.2f} por esse item')
    total += item_value
    more = str(input('Deseja continuar?[S/N] ')).lower()[0]
    if more == 'n':
        break
print(f'O total da sua compra deu R${total:.2f}')
