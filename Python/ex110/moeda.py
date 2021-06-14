def aumentar(preco = 0, taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res) # retorne o res se o format for falso, se nao, chame o metodo moeda

def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato=False):
    res =  preco * 2
    return res if formato is False else moeda(res)


def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',') # linha pra formatação bonitinha


def resumo(preco=0, taxaau=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaau}% de aumento: \t{aumentar(preco, taxaau, True)}') # \t tabulaçao = ficar bonitinho
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)