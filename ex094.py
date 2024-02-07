pessoas = dict()
cadastro = list()
mulheres = list()
media = list()
while True:

    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [F/M]')).upper()
    while pessoas['sexo'] not in 'FM':
        pessoas['sexo'] = str(input('Inválido tente novamente> Sexo: [F/M]')).upper()
    pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    opc = str(input('Deseja adicionar mais pessoas? [S/N] ')).upper()
    while opc not in 'SN':
        opc = str(input('OPÇÃO INVÁLIDA, DESEJA ADICIONAR? [S/N] ')).upper()
    if opc == 'N':
        break
m = 0
for c in cadastro:
    if c['sexo'] == 'F':
        mulheres.append(c)
for c in cadastro:
    for k, v in c.items():
        if k == 'idade':
            m = m + v
m = m / len(cadastro)


for c in cadastro:
    if c['idade'] >= m:
        media.append(c)

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade do grupo é {m} anos')
print('=' *30)
print('As mulheres cadastradas foram:')
if len(mulheres) > 0:
    for l in mulheres:
        print(f'{l["nome"]} / ',end=' ' )
else:
    print('Não foram cadastrada nenhuma mulher')
print('='*30)
print('As pessoas com idade acima da media foram: ')

if len(media) > 0:
    for l in media:
        for k, v in l.items():
            print(f'{k}: {v} ', end='')
        print()
else:
    print('Não possui ninguem acima da idade média')
