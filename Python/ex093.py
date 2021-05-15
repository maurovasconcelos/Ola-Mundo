jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c} ?')))
jogador['gols'] =  partidas[:] # cria uma nova key com o nome gols que recebe uma copia do resultado das partidas
jogador['total'] = sum(partidas) # key total recebe "sum" soma das partidas
print('-=' * 30)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, n in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {n} gols.')
print(f'Foi um total de {jogador["total"]} gols.')