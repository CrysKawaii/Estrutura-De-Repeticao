num = int(input('Digite um número: '))
# esse primeiro laço vai até o número digitado, começando do 2
for c in range(2, num + 1):
    prime = True
    # esse segudno verifica cada número entre 2 e o número digitado menos um
    for i in range(2, c):
        # aqui é feita a verificação para ver se é encontrado algum número que é divisível não só por 1 e ele mesmo
        if c % i == 0:
            # se for o caso a variável revebe False e o laço termina
            prime = False
            break
    # aqui mostra os números primos
    if prime:
        print(c)
