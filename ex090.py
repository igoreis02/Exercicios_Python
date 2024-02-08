alunos = dict()
cadastro = list()

while True:
    alunos['nome'] = str(input('Nome do aluno: '))
    alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))

    if alunos['media'] >= 7:
        alunos['situacao'] = 'Aprovado'
    elif 5 <= alunos['media'] < 7:
        alunos['situacao'] = 'Recuperação'
    else:
        alunos['situacao'] = 'Reprovado'
    cadastro.append(alunos.copy())
    opc = str(input('Deseja adicionar outro aluno? [S/N]')).upper()
    while opc not in 'SN':
        opc = str(input('Opção inválida > Deseja adicionar outro aluno? [S/N]')).upper()
    if opc == 'N':
        break
print('-'*30)
for c in cadastro:
    for k, v in c.items():
        print(f'{k}: {v}')
    print('-'*30)
