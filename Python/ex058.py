from random import randint
computador = randint(0,10)
print('Sou seu cumputador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou! Ao todo você deu {} palpites '.format(palpites))