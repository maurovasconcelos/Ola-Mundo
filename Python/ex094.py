galera = [] # galera é uma lista com vacrios dissionarios, que sao as pessoas
pessoa = {} # cada pessoa é um dicionario diferente que contem nome idade e sexo de cara e uma copia é armazenada na lista galera
soma = 0
while True: #repita eternamente
    pessoa.clear() #limpa a galera
    pessoa['nome'] = str(input('Nome: ')) #pessoa na chave 'nome', vai receber o valor 'Fulano'
    while True: #depois de rodar o de cima vai rodar esse logo em seguida
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #sexo é uma str
        if pessoa['sexo'] in 'MF': # se a resposta acima for 'MF' caga pro print de bobão e passa pra proxima chave que é 'idade'
            break
        print('ERRO! por favor, digite apenas M ou F.') # print de bobão
    pessoa['idade'] = int(input('Idade: ')) #pessoa na chave idade vai receber um numero
    soma += pessoa['idade']
    galera.append(pessoa.copy()) # galera vai receber uma copia dos dados dessa pessoa
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0] # loop basico
        if resp in 'SN': # s
            break
        print('Erro! Responda apenas S ou N.') # print de bobão
    if resp == 'N': # se for nao, para tudo
        break
print('-=' * 30)
print(f'a) Ao todo temos {len(galera)} pessoas cadastradas.') #len, ce ja ta ligado ne
media = soma / len(galera) # media é a variavel soma que é a idade de todos juntos / quantidade de gente da lista
print(f'b) A média de idade é de {media:5.2f} anos') # media é igual a media =:5.2f
print('c) As mulheers cadastradas foram ', end='') #
for p in galera: # pra cada pessoa em galera
    if p['sexo'] in 'Ff': # se a pessoa tiver F no sexo, obviamente ela é mulher...
        print(f'{p["nome"]} ', end='')# printa o nome da pessoa com "sexo F"
print()
print('d) Lista das pessoa que estáo acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')