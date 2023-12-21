soma = 0
cont = 0
for c in range(1, 501, 2):#aqui ja esta pegando os valores impares
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print('A soma de todos os {} valores solicitados é {} '.format(cont, soma))
