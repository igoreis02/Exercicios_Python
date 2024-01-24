palavra = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
