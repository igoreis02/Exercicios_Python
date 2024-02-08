from random import  randint
from  time import  sleep
from  operator import itemgetter

jogo = {
        'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
       }
ranking = dict()
print('Sorteio: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} do dado')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)  # ordena um dicionario tem que importar uma biblioteca reveser = true para ser do maior pra o menor

print('-'*30)
for i, v in enumerate(ranking):
    print(f'{i} LUGAR: {v[0]} com {v[1]}')
