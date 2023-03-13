goku = luffy = ichigo = ippo = null_vote = blank_vote = total =  0
print('===== CANDIDATOS =====')
print('''
1 - GOKU
2 - LUFFY
3 - ICHIGO
4 - IPPO 
5 - VOTO NULO
6 - VOTO BRACNO
''')
while True:
    vote = int(input('Digite seu voto: '))
    if vote == 0:
        break
    elif vote == 1:
        goku += 1
    elif vote == 2:
        luffy += 1
    elif vote == 3:
        ichigo += 1
    elif vote == 4:
        ippo += 1
    elif vote == 5:
        null_vote += 1
    elif vote == 6:
        blank_vote += 1
    else:
        print('Opção inválida!')
    total += 1
percentage_null = null_vote * 100 / total
percentage_blank = blank_vote * 100 / total
print(f'Foram registrados {total} votos')
print(f'O total de voto do candidato 1 é {goku}')
print(f'O total de voto do candidato 2 é {luffy}')
print(f'O total de voto do candidato 3 é {ichigo}')
print(f'O total de voto do candidato 4 é {ippo}')
print(f'O total de votos nulo é {null_vote}')
print(f'O total de votos em branco é {blank_vote}')
print(f'A porcentagem de votos nulos sobre o total é de {percentage_null:.1f}%')
print(f'A porcetagem de votos em branco sobre o total é de {percentage_blank}%')
