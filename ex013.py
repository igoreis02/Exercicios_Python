salario = float(input('Qual o salário do funcionário? R$'))
reajuste = (salario*15)/100
print('um funcionário que ganhava R${:2}, com 15% de aumento, passa a  receber R${:4}'.format(salario, salario+reajuste))
