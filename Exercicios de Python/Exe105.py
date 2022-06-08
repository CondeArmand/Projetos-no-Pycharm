def notas(*n, sit=False):
    """
    -> Analisador de situação de notas
    :param n: Recebe um número n de notas
    :param sit: Parametro opcional para exibição ou não da situaçõa
    :return: Retorna um dicionario com os valores informados.
    """
    dic = dict()
    dic['Total'] = len(n)
    dic['Maior nota'] = max(n)
    dic['Menor nota'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        dic['Situação'] = 'RUIM' if dic['Média'] < 5 else 'RAZOAVEL' if 5 >= dic['Média'] < 7 else 'BOA'
    return dic


resp = notas(10, 8, 3, 7, 8, 3, 4, 5, 5, sit=True)
print(resp)