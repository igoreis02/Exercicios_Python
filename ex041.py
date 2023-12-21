from random import randint
from time import sleep
lista = ('pedra', 'papel', 'tesoura')
print('='*25)
print('0 - Pedra')
print('1 - Papel')
print('2 - Tesoura')
print('='*25)
jogador = int(input('Qual deseja jogar? '))
computador = randint(0,2)

if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
if computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
if computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')


print('Você: {} computado: {}'.format(lista[jogador], lista[computador]))

