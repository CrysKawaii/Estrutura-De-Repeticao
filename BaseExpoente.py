base = int(input('Digite a base: '))
exponent = int(input('Digite o expoente: '))
result = 1
for c in range(exponent):
    result *= base
if exponent == 0:
    result = 1
print(result)
