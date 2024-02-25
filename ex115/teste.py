from ex115.lib.interface import *
from time import  sleep
while True:
    res = menu(['Ver pessoas Cadastradas' , 'Cadastra nova pessoa', 'Sair do Sistema'])
    if res == 1:
        cabecalho('Pessoas Cadastradas')
    elif res == 2:
        cabecalho('Cadastra nova pessoa')
    elif res == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção invalida\033[m')
    sleep(2)