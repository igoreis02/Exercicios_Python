from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome,'rt') #rt leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nome):
    try:
        a = open(nome,'wt+') #abre o arquivo de testo e o mais é se nao tiver ele cria o arquivo
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a =open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.readlines()) mostra todo o arquivo em uma linha
        for k,linha in enumerate(a):
            dado = linha.split(';')#retira o ; para mostra
            dado[1] = dado[1].replace('\n','') #esta trocando a quebra de linha apos a idade por nada
            print(f'{k:<2}{dado[0]:<25}{dado[1]} anos')
    finally:
        a.close()


def cadastrar (arq,nome='Desconhecido',idade=0):

    try:
        a = open(arq,'at') #a == append abrindo o arquivo para adicionar t ==  texto
    except:
        print('Ouve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n') #escreve dentro do arquivo
        except:
            print('Ouve um erro na hora de escreve os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def deletar(arq):
    try:
        a = open(arq,'r+')
    except:
        print('Erro')
    else:
        a.truncate(0)
    finally:
        a.close()


def deletarCadastro(arq):
    lerArquivo(arq)
    try:
        a = open(arq,'rt')
        linha = a.readlines()
        a.close()
        n = leiaInt('Qual indice: ')
        a = open(arq,'w')
        for k,l in enumerate(linha):
            if k != n:
                a.write(l)
        print('Deletado...')
        a.close()
    except:
        print('Erro!')