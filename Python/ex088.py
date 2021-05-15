from random import randint
from time import sleep
lista= [] # uma lista com a lista dos jogos dentro
jogos = [] # quantidade de vezes que vc vai querer ver o resultado rolando
print('-=' * 30)
print('     JOGA NA MEGA SENA     ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie ?')) # quantos jogos quer ver
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) # jogos vai receber a copia do que estiver na lista
    lista.clear() # limpa a lista
    tot += 1
print(f'SORTEANDO {quant} JOGOS ')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' *5, '< Boa Sorte >', '-=' *5)