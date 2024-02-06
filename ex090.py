alunos = dict()

alunos['nome'] = str(input('Nome do aluno: '))
alunos['media'] = float(input('Media do aluno: '))

for k, v in alunos.items():
    print(f'{k}: {v}')

if alunos['media'] >= 7:
    print('Sutuação: Aprovado')
else:
    print('Situação: Reprovado')

