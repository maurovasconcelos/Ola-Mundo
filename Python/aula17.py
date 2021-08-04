num = [2,5,9,1]
num[2] = 3 # nas listas da pra substituir indices
num.append(7) # append =  comando inserir novo numero/flinstons na lista
num.sort(reverse=True) # sort = organizar ordem crescente, reverse adivinha o que faz...
num. insert(2, 0) # inserir na posição 2 o numero 0
num.pop(2) # comando .pop pra remover um indice, se o () tiver vazio, remove o ultimo indice, se nao, EX: (2) remore quem tiver na posição 2 da lista
print(num)
print(f'Essa lista tem {len(num)} elementos.') # não esquece, len, mostrar quantos elementos tem na lista
print('-=-' * 60)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # = tipo um contador, v são os valores.
    print(f'Na posição {c} encontrei o valor {v}!') # na posição 'c' = contador, encontrei o valor 'v' = valor
print('Cheguei ao final da lista.')
#---------------------------------------------------------------------------------------------------------------------------------
print('-=-' * 60)
valor = list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor: ')))

for c, v in enumerate(valor): # = tipo um contador, v são os valores.
    print(f'Na posição {c} encontrei o valor {v}!') # na posição 'c' = contador, encontrei o valor 'v' = valor
print('Cheguei ao final da lista.')

#-----------------------------------------------------------------------------------------------------------
a = [2, 3, 4, 7]
b = a[:] # [:] comando pra copiar a lista, obs: não substitui a lista a, sim copia os valores
b[2] = 8 # o indice 2 na lsita A vai reber 8 na lista B, sacou ? izi
print(f'Lista A: {a}')
print(f'Lista B: {b}')