#IMCOMPLETO !!!!
preco = float(input('Digite o valor do produto: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] Á vista dinheiro/débito')
print('[ 2 ] Á vista no cartão/credito')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 /100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela = total / vezes
    vezes = int(input('Vai dividir de quantas vezes? :')
    print('Sua compra será parcelada de {}x de R${:.2f}'.format(vezes, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

