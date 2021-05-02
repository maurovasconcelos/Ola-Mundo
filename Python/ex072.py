cont = ('zero', 'um','dois','tres','quatro','cinco'
        ,'seis','sete','oito','nove','dez','onze',
        'doze','treze','catorze','quinze','dezesseis'
        ,'dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20: #feito pra quando digitar algo que nao seja entre 0 e 20, continuar no loop
        break
    print('Tente novamente. ', end='')
    print(f'Você digitou o numero {cont[num]}')
print('Acabou')