teste = []
teste.append('Mauro')
teste.append(22)
galera = []
galera.append(teste[:]) # comando copiar
teste[0] = 'Ximas'
teste[1] = 23
galera.append(teste[:]) # galera vai receber uma copia do teste
print(galera)
print('-=' * 30)

#-----------------------------------------------------------------------------------------------------------------------
galera2 = [['João', 19],['Ana', 33],['Marcos', 38],['José', 78]]
for p in galera2: # pra cada pessoa da lista galera2, faça:
    print(f'{p[0]} tem {p[1]} anos de idade.')# me mostre a pessoa 0=nome/primeiro item da lista e tem p[1]= segundo item da lista que no caso é a idade
print('-=' * 30)

#-----------------------------------------------------------------------------------------------------------------------


galera3 = []
dado = []
totmen = totmai = 0
for c in range(0,7): #  "repita" x vezes
    dado.append(str(input('Nome: '))) # os dados vão pra lista
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:]) # a lista galera recebe uma copia dos dados [:]=Comando pra copiar
    dado.clear() # os dados são excluidos mais fica suave que a copia ta salva na lista galera3
print(galera3)


for pessoas in galera3: # pra cada pessoa ne galera 3 faça:
    if pessoas[1] >= 21:  #se a idade for >= 21:
        print(f'{pessoas[0]} é maior de idade.')
        totmai += 1  # se fulano tiver a idade >=21 o total de nego maior de idade recebe +1
    else:
        print(f'{pessoas[0]} é menor de idade.')
        totmen += 1 #...
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
