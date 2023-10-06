a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro valor: '))
#verifica quem é o menor
menor = a
if (b < a) and (b < c):
    menor = b
if (c < b) and (c < a):
    menor = c
#verifica quem e o maior
maior = a
if (b > a) and (b > c):
    maior = b
if (c > b) and (c > a):
    maior = c
print('O menor valor Digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
