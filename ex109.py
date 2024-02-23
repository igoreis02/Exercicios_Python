import ModuloEx107and108
p = float(input('Digite o preço: R$'))
print(f'A metade do {ModuloEx107and108.moeda(p)} é {ModuloEx107and108.metade(p,r=True)}')
print(f'O dobro do {ModuloEx107and108.moeda(p)} é {ModuloEx107and108.dobro(p,r=True)}')
print(f'Aumentando 10% temos: {ModuloEx107and108.aumentar(p,10,r=True)}')
print(f'Reduzindo 13% temos: {ModuloEx107and108.diminuir(p, 13,r=True)}')
