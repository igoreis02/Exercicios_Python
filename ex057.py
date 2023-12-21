sexo = str(input('Qual o seu sexo (F OU M):')).strip().upper()[0] #tira os espaços, joga para maiusculo a primeira e pega somente a primeira letra
while sexo not in 'FM': #nao estiver em feminino ou masculino
        sexo = str(input('Sexo invalido, digite novamente: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))
