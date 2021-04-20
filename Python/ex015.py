dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
dias = dias * 60
# Da pra fazer melhor
km = km * 0.15
print('O valor a pagar pelo aluguel é de {:.2f}'.format(dias + km))

