produto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros',34.90)

print('-'*40)
print(f'{"Listagem de preços":^40}')# 40 espaços centralizado :^
print('-'*40)
for cont in range(0, len(produto), 2):
    print(f'{produto[cont]:.<30} R$ {produto[cont+1]:.2f}') #:<30 a esquerda com os ponto  > a direita
