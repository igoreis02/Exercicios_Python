from datetime import date


def voto(nascimento):
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade <= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGÁTORIO'


nasc = int(input('ANO DE NASCIMENTO: '))
print(voto(nasc))
