preco = float(input('Qual o preço do produto ? R$'))
novo = preco - (preco * 5 / 100)
print(f'O preço do produto é R${preco:.2f} e com desconto, sai a R${novo:.2f} com um desconto de 5%')

