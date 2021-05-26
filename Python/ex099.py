def maior(* num): #
    cont = maior = 0 # contador e maior = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for valor in num: # para cada valor nos numeros
        print(f'{valor} ', end='', flush=True) # mostre os
        if cont == 0:#comando basico maior
            maior = valor
        else:
            if valor > maior:# se o valor for maior que o maior numero digitado ate entao, ele se torna o maior
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior informado foi {maior}.')


#programa principal / Chamando a função já com os valores que eu quero,
maior(2, 9, 6, 8, 3, 0, 4, 5)
maior(5, 8, 6, 3)
maior(5, 3, 0)
maior(6)