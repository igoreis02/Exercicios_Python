import random
aluno1 = str(input('1º Aluno(a)'))
aluno2 = str(input('2º Aluno(a)'))
aluno3 = str(input('3º Aluno(a)'))
aluno4 = str(input('4º Aluno(a)'))

lista = [aluno1, aluno2, aluno3, aluno4]
aleato = random.choice(lista) #Pega um  aleatorio
print('Aluno aleatorio {}'.format(aleato))

random.shuffle(lista) #embaralha a lista
print(lista)

