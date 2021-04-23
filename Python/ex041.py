from datetime import  date
ano = float(input('Qual o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print('Você tem {} anos, categoria MIRIN!'.format(idade))
elif idade <=14:
    print('Você tem {} anos, categoria INFANTIL'.format(idade))
elif idade <=19:
    print('Você tem {} anos, categoria SENIOR'.format(idade))
