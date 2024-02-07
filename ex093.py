jogo = dict()
gols = list()
qtd = 0

jogo['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidade {jogo["jogador"]} jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos Gols na partida {c}? ')))
    qtd += gols[c]
jogo['gols'] = gols
jogo['total'] = qtd
print('='*30)
print(jogo)

print('='*30)
print(f'O campo nome tem o valor {jogo["jogador"]}')
print(f'O campo gol tem o valor {jogo["gols"]}')
print(f'O campo total tem o valor {jogo["total"]}')

print('='*30)
for c in range(len(gols)):
    print(f'=> Na partida {c}, fez {jogo["gols"][c]} gols')
print(f'Foi um total de {jogo["total"]} gols')
