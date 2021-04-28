print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10: # se o contador for menor ou igual a 10 faça:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim...')