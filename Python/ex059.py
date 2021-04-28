n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual é a sua opção ? '))
    if opção == 1: # se a opção for 1 faça:
        soma = n1 + n2
        print('A soma entre {} e {}, é {}'.format(n1, n2, soma))
    elif opção == 2: # se for 2
        multi = n1 * n2
        print('A multiplicação de {} e {}, é igual {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 =  int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('-=-' * 10)
print('Fim do programa! Volte sempre!')