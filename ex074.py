from random import randint
menor = maior = 0
tupla = (randint(0, 10), randint(0, 20), randint(0, 40), randint(0, 50), randint(0, 30))

print('Os números sorteados foi: ', end='')
for cont in range(0,5):
    print(tupla[cont], end=' ')
print(f'\nO menor número da tupla é: {min(tupla)}') #Mostra o maior valor da tupla
print(f'O maior número da tupla é: {max(tupla)}') #Mostra o menor valor da tupla
