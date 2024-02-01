alunos = list()
cadastro = list()

'''
solução do professor 
ficha = list()

nome = str(input('Nome: '))
nota1 = float(input('Nota1:) )
nota2 = float(input('Nota2: '))
media = (nota1 + nota2)/2

ficha.append([nome, [nota1, nota2], media]) listas compostas
'''

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Nota 1: ')))
    cadastro.append(float(input('Nota 2: ')))
    media = (cadastro[1]+cadastro[2])/2
    cadastro.append(media)

    alunos.append(cadastro[:])
    cadastro.clear()

    opc = str(input('Deseja continuar? [S/N]')).upper()
    while opc not  in 'SN':
        opc = str(input('Opção invalida, Deseja continuar? [S/N]')).upper()
    if opc in 'N':
        break
print('='*25)
print(f'{"No.":<2}  {"NOME": <10} {"MÉDIA":>8} ')
print('-'*25)
for i, c in enumerate(alunos):
    print(f'{i:<4} {c[0]: <10} {c[3]:>8.1f}')

while True:
    opc = int(input('Mostra nota de qual Aluno? finalizar digitar -1'))
    if opc < 0:
        print('Finalizando...')
        break
    if opc <= len(alunos) - 1:
        print(f'Nota de {alunos[opc][0]} são: {alunos[opc][1]} / {alunos[opc][2]}')
