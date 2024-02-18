jogo = dict()
gols = list()
time = list()
qtd = 0
pos = 0
while True:
    jogo.clear()
    jogo['jogador'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidade {jogo["jogador"]} jogou? '))
    gols.clear()
    for c in range(0,partidas):
        gols.append(int(input(f'    Quantos Gols na partida {c+1}? ')))
        qtd += gols[c]
    jogo['gols'] = gols[:]
    jogo['total'] = qtd
    time.append(jogo.copy())
    print('='*30)

    opc = str(input('Quer continuar? [S/N]')).upper()
    while opc not in 'SN':
        opc = str(input('Opção inválida > Quer continuar? [S/N]')).upper()
    if opc in 'N':
        break

print('-'*40)
print('Cod ',end='')
for i in jogo.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for c, v in enumerate(time):
    print(f'{c:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostra dados de qual Jogador? (999 para parar)  ' ))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe Jogador com o codigo {busca}')
    else:
        print(f'Levantamento do Jogador {time[busca]["jogador"]}')
        for i , v in enumerate(time[busca]["gols"]):
            print(f'    No Jogo {i+1} fez {v}')
