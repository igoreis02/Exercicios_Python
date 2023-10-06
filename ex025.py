from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
aleatorio = randint(0, 5)
num = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if num == aleatorio:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(aleatorio, num))
