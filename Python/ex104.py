def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        ok = True
    else:
        print('Erro! digite um valor inteiro.')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
