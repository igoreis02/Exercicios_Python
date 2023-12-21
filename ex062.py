pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = pri_termo + (10-1) * razao
#for c in range(pri_termo, decimo+razao, razao):
 #   print('{}'.format(c), end=' -> ')
termo = pri_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos temos você quer mostrar  a mais ?'))
print('Fim')

