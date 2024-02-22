def notas(*num,sit=False):
    '''
    -> função para analizar notas e situaçoes de varios alunos
    :param num: uma ou mais notas de alunos
    :param sit: opicional indicando a situação
    :return: dicionario com informaçoes da turma
    '''

    print('-'*30)
    lista = dict()
    maior = menor = soma = 0
    media = 0
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['media'] = sum(num)/len(num)
    if sit:
        if lista['media'] >= 7:
            lista['situacao'] = 'OTIMO'
        elif lista['media'] >= 5:
            lista['situacao'] = 'BOM'
        else:
            lista['situacao'] = 'RUIM'

    return lista


res = notas(10.0, 5.5, 2.5, 6.5, sit=True)
print(res)
