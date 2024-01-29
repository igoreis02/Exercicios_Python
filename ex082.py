lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um número: ')))

    #if numero % 2 == 0:
        #par.append(numero)
    #else:
        #impar.append(numero)

    opc = str(input('Deseja continuar? [S/N]')).upper()
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper()
    if opc in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('='*30)
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {par}')
print(f'A lista de Ímpares é {impar}')
