pri_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = pri_termo + (10-1) * razao
for c in range(pri_termo, decimo+razao, razao):
    print('{}'.format(c), end=' -> ')

