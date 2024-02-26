from ex115.lib.interface import *
from ex115.lib.arquivos import *
from time import  sleep

arq = 'Cadastro.txt'
if not arquivoExiste(arq):
    criaArquivo(arq)
indice = 1

while True:

    res = menu(['Ver pessoas Cadastradas' , 'Cadastra nova pessoa', 'APAGAR TODO ARQUIVO','APAGAR CADASTRO PELO INDICE ','Sair do Sistema'])
    if res == 1:
        #Opção de lista o conteudo de um arquivo
        lerArquivo(arq)
    elif res == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
        indice += 1
    elif res == 3:
        cabecalho('DELETANDO DADOS DO ARQUIVO TXT ')
        deletar(arq)
    elif res == 4:
        cabecalho('DELETANDO CADASTRO')
        deletarCadastro(arq)
    elif res == 5:
        cabecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção invalida\033[m')
    sleep(2)
