pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = pri_termo + (10-1) * razao
#for c in range(pri_termo, decimo+razao, razao):
 #   print('{}'.format(c), end=' -> ')
termo = pri_termo
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
