distancia = int(input('São quantos km de viagem? '))
print('Você está prestea a fazer uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será d R${:.2f}'.format(preco))