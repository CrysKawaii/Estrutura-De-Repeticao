a = 80000
b = 200000
years = 0
while True:
    years += 1
    print(f'População A no ano {years}: {int(a)}')
    print(f'População B no ano {years}: {int(b)}')
    a += (a * 3 / 100)
    b += (b * 1.5 / 100)
    if a >= b:
        break
print(f'Depois de {years} anos a população A passou a B')
