lista = []
dadostemp = []
men = mai = 0
while True:
    dadostemp.append(str(input('Digite um nome: ')))
    dadostemp.append(float(input('Quantos Kg ?: ')))
    if len(lista) == 0: # se eu nao coloquei ninguem na listao maior = menor = dadostemp[1] <- temp na posição 1 é o numero/ idade
        mai = men = dadostemp[1]
    else:
        if dadostemp[1] > mai: # se o valor de temp1 for maior que o maior, ele recebe o titulo de maior
            mai = dadostemp[1]
        if dadostemp[1] < men: # se o valor de temp1 for menor que o menor valor digitado, ele se tornaraá o menor
            men = dadostemp[1]

    lista.append(dadostemp[:])
    dadostemp.clear()
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(lista)
print(f'Ao todo você cadastrou {len(lista)} pessoas.') # len= quantidade de pessoas cadastradas
print(f'O maior peso foi de {mai}Kg')
for p in lista: # pra cada pessoa na lista faça:
    if p[1] == mai: # se o peso= p[1] for igual o maior...
        print(f'{p[0]} ') # mostre o nome da pessoa(s)
print(f'O menor peso foi de {men}Kg. ', end='')
for p in lista:
    if p[1] == men: # se o peso for menor, mostre o nome da pessoa com o menor peso
        print(f'{p[0]}, ', end='')