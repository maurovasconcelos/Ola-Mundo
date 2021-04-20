preco = float(input('Qual o preço do produto ? R$'))
novo = preco - (preco * 5 / 100)
print('O preço do produto é R${:.2f} e com desconto, sai a R${:.2f}'.format(preco + novo))

