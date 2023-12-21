valor_casa = float(input('Qual o valor do imovél ?'))
salario = float(input('Qual o seu salário?'))
tempo = float(input('Quantos anos de pagamento?'))
prestacao = valor_casa / (tempo * 12)
valor_porcentagem = (salario * 30)/100
if prestacao > valor_porcentagem:
    print('Infelizmente você não pode realizar o financiamento!')
else:
    print('Financiamento APROVADO')
