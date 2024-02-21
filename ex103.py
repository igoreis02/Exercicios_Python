def ficha(jogador='desconhecido', gol=0):
    print(f'o Jogador <{jogador}> fez {gol} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric(): # vendo se o valor da string pode ser um numero
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '': # verifica se a string tem dados
    ficha(gol=gol)
else:
    ficha(nome,gol)
