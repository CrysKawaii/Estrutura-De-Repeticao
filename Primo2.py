num = int(input('Digite um número: '))
count = 0
for c in range(1, num + 1):
    if num % c == 0:
        count += 1
if count == 2:
    print('Esse número é primo!')
else:
    print('Não é primo!')
    print('Ele é divisível por:', end=' ')
    for c in range(1, num + 1):
        if num % c == 0:
            print(c, end=' ')
