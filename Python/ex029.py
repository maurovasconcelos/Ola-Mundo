vel = float(input('Qual é a velocidade atual do carro? '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tu ta correndo irmão, ta crazy?')
    multa = (vel - 80) * 7 #Pega a visão, a variavel multa recebe a variavel vel - o valor - o numero permitido pelo flinstons * 7
    print('Você foi multado e tera de pagar a multa no valor de R${}'.format(multa))