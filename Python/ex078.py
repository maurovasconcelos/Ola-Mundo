listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor par a Posição {c}:')))
    if c == 0:
        mai = men = listanum[c] # se o C for igual a 0 o maior e o menos vão ser 0 //IMPORTANTE: Quando o C for qualquer valor, esse valor é o maior e o menor ao msm tempo
    else:
        if listanum[c] > mai: # se o valor na posição C, for maior que o "antigo maior", ele se tornará o maior
            mai = listanum[c]
        if listanum[c] < men: # se o valor na posição C, for menor que o "antigo menor", ele se tornará o menor
            men = listanum[c]
print('-=-' * 30)
print(f'Você digiotu os valores {listanum}')
print(f'O maior valor digitado foi: {mai} nas posições ', end='')
for i, v in enumerate(listanum): # para o indice e o valor, enumeramos a lista...
    if v == mai: # se o valor for igual o maior numero...
        print(f'{i}...', end='') # me mostre o indice/ quais posições o maior valor está
print()
print(f'O menor valor digitado foi: {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men: # se o valor for igual o menor numero me mostre
        print(f'{i}...', end='')# quais posiçoes o menor valor está
print()