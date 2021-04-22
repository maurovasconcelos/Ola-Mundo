emprestimo = float(input('Qual o valor da casa que deseja comprar R$ '))
salario = float(input('Qual o valor do seu salário R$ '))
anos = int(input('Em quantos anos pretende pagar a casa ? '))
prestacao = emprestimo / (anos * 12)
# pega a visao, a prestação é o valor da casa / pela quantidade de anos * 12, que sao quantos meses tem ao ano, parece dificil mais é só isso
minimo = salario * 30 /100 #variavel minimo é justamente o minimo possivel do salaraio e caso exceda o minimo da ruim
print('Para pagar uma casa de R${:.2f} em {} anos'.format(emprestimo, anos))
print('A prestação será de R${:.2f} ao mês.'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo concedido, PARABÈNS!')
else:
    print('Eprestimo NEGADO, Sorry !')