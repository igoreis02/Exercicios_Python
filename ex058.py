from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
computador =randint(1,10)
acertou  = False
palpites = 0
while not acertou:
    jogador = int(input('Em que número eu pensei?'))
    print('PROCESSANDO...')
    sleep(3)
    if (jogador == computador):
        print('PARABÉNS! Você conseguiu me vencer.')
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez ')
        else:
            print('Menos... Tente mais uma vez ')
    palpites += 1
print('Foram {} palpites até acertar'.format(palpites))
