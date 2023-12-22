from datetime import date
maior = qtdH = qtdM =0
print('-'*20)
print('Cadastro de pessoa')
while True:
    print('-'*20)
    anoN = int(input('Qual seu ano de nacimento? '))
    anoA = date.today().year
    idade = anoA - anoN

    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo? [F/M')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        qtdH += 1
    if idade < 20 and sexo == 'F':
        qtdM += 1

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja Continuar? [S/N')).upper().strip()[0]
    if opc == 'N':
        break
print('-'*20)
print(f'Total de pessoas com mais de 18 anos : {maior}')
print(f'Ao todo temos {qtdH} homens cadastrados')
print(f'E temos {qtdM} mulheres com menos de 20 anos')
