time = []
jogador = {}
partidas = []
while True:
    jogador.clear() #limpar o dicionario jogador antes do loop pegar o proximo
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))# tot = total de partidas que vai jogar
    partidas.clear() # novamente limpar a lista partidas
    for c in range(0, tot): # pro contador no range 0 até o tot
        partidas.append(int(input(f'Quantos gols na partida {c+1} ?'))) #
    jogador['gols'] =  partidas[:] # cria uma nova key com o nome gols que recebe uma copia do resultado das partidas
    jogador['total'] = sum(partidas) # key total recebe "sum" soma das partidas
    time.append(jogador.copy()) # time recebe uma copia dos dados do jogador
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Resposta incorreta, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys(): #pra cada indice nas chaves faça
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.  ')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')