from random import randint
from  time import  sleep
qtdAposta = cont = qtd =  0
sorteio = list()
aposta = []

print('-'*30)
print(f'       JOGA NA MEGA SENA      ')
print('-'*30)

qtdAposta = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'========== Sorteando {qtdAposta} Jogos ==========')
while qtd < qtdAposta:
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont == 6:
            sorteio.sort()
            aposta.append(sorteio[:])
            sleep(1)
            print(f'Jogo {qtd+1}: {aposta[qtd]}')
            sorteio.clear()
            cont = 0
            break
    qtd += 1
print('==' * 5, '< Boa Sorte >', '==' * 5)

#print(f'========== Sorteando {qtdAposta} Jogos ==========')
#for i, c in enumerate(aposta):
    #sleep(1)
    #print(f'Jogo {i + 1}: {c}')
