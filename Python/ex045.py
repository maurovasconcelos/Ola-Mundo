from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # Pc randomiza 3 opçoes
print('O computador escolheu {}'.format(itens[computador])) #vai pegar o valor que o pc randomizou com o nome referente a lista ex: 0 = pedra 1 = papel 2 = tesoura
print('''Sua opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-'*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*15)
if computador == 0: # pc jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador ==2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # pc jogou papel
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador ==2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # pc jogou tesoura
    if jogador == 0:
        print('VOCÊ GANHOU !')
    elif jogador == 1:
        ('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
else:
        print('JOGADA INVALIDA!')