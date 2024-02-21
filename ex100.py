from random import randint
from time import sleep


def escreva():
    print('-'*40)

def sortear(n,lista):
    if n == 0:
        print('Erro valor 0')
    else:
        print(f'Sorteando {n} valores da lista:', end=' ')
        for c in range(0, n):
            lista.append(randint(1,10))
            sleep(0.5)
            print(lista[c], end=' ')
        print('Pronto! ')


def somaPar(l):
    sp = 0
    print(f'Somando os valores pares de {lista}, temos ',end=' ')
    for c in lista:
        if c % 2 == 0:
            sp += c
    print(sp,end=' ')
    print()


def somaImpar(l):
    si = 0
    print(f'Somando os valores ímpar de {lista}, temos ', end=' ')
    for c in lista:
        if c % 2 == 1:
            si += c
    print(si,end=' ')
    print()


lista = list()

while True:
    s = int(input('Sortear quantos Números? '))
    sortear(s,lista)
    while True:
        opc = str(input('Deseja saber a soma dos Pares [P] soma dos impares [I] ?  Não saber: [N]')).upper()
        while opc not in 'NPI':
            opc = str(input('OPÇÃO INVÁLIDA > Deseja saber a soma dos Pares [P] soma dos impares [I] ? Não saber: [N]')).upper()
        if opc in 'P':
            somaPar(lista)
        elif opc in 'I':
            somaImpar(lista)
        elif opc in 'N':
            break

    opc = str(input('Deseja sortear mais numeros [S/N]')).upper()
    lista.clear()
    while opc not in 'SN':
        opc = str(input('OPÇÃO INVÁLIDA > Deseja sortear outros numeros [S/N]')).upper()
        lista.clear()
    if opc == 'N':
        break
