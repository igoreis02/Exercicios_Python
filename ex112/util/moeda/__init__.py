def metade(n=0, r=True):
    res = n/2
    return res if r == False else moeda(res)


def dobro(n=0, r=True):
    res = n * 2
    return res if r == False else moeda(res)


def aumentar(num=0, porcentagem=0, r=True):
    soma = num + (num * porcentagem/100)
    return soma if r == False else moeda(soma)


def diminuir(num=0, porcentagem=0,r=True):
    subtrair = num - (num * porcentagem/100)
    return subtrair if r == False else moeda(subtrair)


def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def escreva(msg):
    tam = len(msg)+15
    print('-' * tam)
    print('msg'.center(tam))
    print('-' * tam)

def resumo(preco=0, aumento=0,reducao=0):
    escreva('RESUMO DO VALOR')
    print(f'{"Preço analizado:"} {moeda(preco):>13}')
    print(f'Dobro do Preço: {dobro(preco):>14}')
    print(f'Metade do Preço: {metade(preco):>13}')
    print(f'{aumento}% de Aumento: {aumentar(preco,aumento):>14}')
    print(f'{reducao}% de Redução: {diminuir(preco,reducao):>14}')
    print('-'*30)