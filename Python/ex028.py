from random import randint
pcnum = randint(0,5) #Faz o computador "pensar"
print('-=-' * 10)
print ('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
if jogador == pcnum:
    print('PARABENS BROTHER, você conseguiu me vencer')
else:
    print('Você foi solaaaado, eu pensei no numero {} e não no {}!'.format(pcnum, jogador))
