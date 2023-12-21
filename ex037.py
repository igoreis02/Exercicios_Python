nota1 = float(input('1ª NOTA: '))
nota2 = float(input('2ª NOTA: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('REPROVADO')
elif media > 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
elif media > 7.0:
    print('APROVADO')
else:
    print('INVÁLIDO')
