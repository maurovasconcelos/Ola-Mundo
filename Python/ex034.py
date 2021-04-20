salario = float(input('Digite seu salario '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Seu salario passara ser R${:.2f} com o aumento de 15%'.format(novo))
else:
    novo = salario + (salario * 10 /100)
    print('Seu salario passara ser R${:.2f} com o aumento de 10% '.format(novo))