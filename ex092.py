from datetime import date
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
anoDeNacimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - anoDeNacimento
pessoa['idade'] = idade
pessoa['ctps'] = int(input('CTPS: (0 não tem)'))

if pessoa['ctps'] != 0:
    pessoa['anoContratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: '))

    contribuicao = ano - pessoa['anoContratacao']
    if contribuicao == 35:
        pessoa['aposentar'] = contribuicao
    elif contribuicao < 35 and contribuicao > 0:
        tempo = 35 - contribuicao
        aposentar = idade + tempo
        pessoa['aposentar'] = aposentar
    elif contribuicao > 35:
        tempo = contribuicao - 35
        aposentar = tempo
        pessoa['aposentar'] = aposentar
    else:
        pessoa['aposentar'] = contribuicao

print(f'Nome: {pessoa["nome"]}')
print(f'Idade: {pessoa["idade"]}')
print(f'CTPS: {pessoa["ctps"]}')
if pessoa['ctps'] != 0:
    print(f'Contratação: {pessoa["anoContratacao"]}')
    print(f'Salário: {pessoa["salario"]}')

    if pessoa['aposentar'] > 35:
        print(f'Você já poderia ter aposentado há: {pessoa["aposentar"]} anos')
    elif pessoa['aposentar'] < 35 and pessoa['aposentar'] >0:
        print(f'Falta {pessoa["aposentar"]} anos para você aposentar')
    elif pessoa['aposentar'] == 35:
        print(f'Já pode aposentar, você contribuiu {pessoa["aposentar"]} anos ')
else:
    print('Você ainda não tem contruibuicão')
