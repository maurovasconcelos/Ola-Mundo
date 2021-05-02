numeros = [] # da pra usar o numeros = list(), mais o [] é mais facil
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros: # se o numero nao tiver na lista, o valor é adicionado
        numeros.append(n)
        print('Valor adicionado com Sucesso...')
    else: # se o numero ja estiver na lista, Valor duplicado, se ferrou
        print('Valor DUPLICADO! Não vou adicionar... ')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn': # se resposta for nao, apre o loop
        break
print('-=-' *30)
numeros.sort() # comando pra colocar em ordem, só
print(f'Você digitou os valores{numeros}')