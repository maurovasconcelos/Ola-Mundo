from datetime import date # importando funcionalidade da biblioteca datetime
atual = date.today().year #comando de data do ano atual
nasc = int(input('Qual o ano do seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade #18 que é a idade pra alistar - a variavel idade, o que restar é o saldo que falta
    print(' Você tem {} anos e ainda não pode se alistar, podera daqui a {} anos.'.format(idade, saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Voce tem {} anos e JÀ PODE SE ALISTAR !!!'.format(idade))
else:
    saldo = idade - 18 #idade - 18 que é a jhonson, o que sobrar é o saldo.
    print('Você ja tem {} anos, ja deveria ter se alistado a {} anos.'.format(idade, saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))