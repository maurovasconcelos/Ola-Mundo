pessoas = {'nome': 'Mauro', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]}, tem {pessoas["idade"]} anos.')
print('=-' * 30)
pessoas['peso'] = 85,5 # nao precisa do append, da pra adicionar dessa forma
#-----------------------------------------------------------------------------------------------------------------------
print(pessoas.keys()) # mostra as chaves de busca na biblioteca
print(pessoas.items()) # mosta os itens da lista
#-----------------------------------------------------------------------------------------------------------------------
for k, v in pessoas.items():
    print(f'{k} = {v}')

#-----------------------------------------------------------------------------------------------------------------------
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['UF']) # se ligou ?, brasil indice 0 mostrando o indice 'UF'

#-----------------------------------------------------------------------------------------------------------------------
estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # a lista brasil vai receber uma copia do dicionario estado  // comando .copy() é equivalente ao .append das listas
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')