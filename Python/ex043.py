peso = float(input('Qual é seu peso ? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura **2)
if imc < 18.5:
    print('VOCÊ ESTÁ MUITO ABAIXO DO PESO !')
elif 18.5 <= imc < 25:
    print('VOCÊ ESTA NA FAIXA DE PESO NORMAL')
elif 25 <= imc < 30:
    print('VOCÊ ESTÁ EM SOBREPESO')
elif 30 <= imc < 35:
    print('VOCÊ TEM OBESIDADE ')
elif 35 <= imc < 40:
    print('VOCÊ TEM OBESIDADE SEVERA')
else:
    print('OBESIDADE MORBIDA')
print('Seu IMC é {:.2f}'.format(imc))
