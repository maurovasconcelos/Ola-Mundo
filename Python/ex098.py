from time import sleep

def contador(i, f, p):# função contador vai receber 3 valores
    print(f'Contagem de {i} até {f} de {p} em {p}')# print pra mostrar os 3
    sleep(1)

    if p < 0:# se o passo for menor que 0/negativo o passo se torna positivo p *= -1
        p *= -1
    if p == 0: # se for 0, se torna 1, nao tem como pular de 0 em 0
        p = 1
    if i < f:# se o inicio for menor que o final, o cont recebe o inicio
        cont = i
        while cont <= f: # enquanto o cont for <= final
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')

#programa principal
#Insere valor
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas) # chamando a função com os valores que o cliente negoçou 