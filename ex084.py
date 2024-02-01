pessoa = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    opc = str(input('Deseja continuar: [S/N] ')).upper()
    while opc not in 'SN':
        opc = str(input('TENTE NOVAMENTE > Deseja continuar: [S/N')).upper()
    if opc in 'N':
        break

print(f'Ao todo, você cadastrou {len(pessoa)} pessoas')
print(f'O maior peso foi de {maior}kg Peso de ',end='')
for p in pessoa:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor}kg Peso de ',end='')
for p in pessoa:
    if p[1] == menor:
        print(f'[{p[0]}]')


