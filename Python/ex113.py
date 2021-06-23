def leiaint(msg):
    while True: #repita infinitamente
        try: #tente
            n = int(input(msg))
        except (ValueError, TypeError): #se o erro for Valuem ou Type, faça:
            print('\033[31mERRO: Por favor, digite  um número inteiro válido.\033[m ')
            continue# ...
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[31m')
            return 0
        else: # se nao/ se nao der erro...
            return n # retorne o valor n, que foi o digitado.


def leiafloat(msg):
    while True: #repita infinitamente
        try: #tente
            n = float(input(msg))
        except (ValueError, TypeError): #se o erro for Valuem ou Type, faça:
            print('\033[31mERRO: Por favor, digite  um número inteiro válido.\033[m ')
            continue# ...
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[31m')
            return 0
        else: # se nao/ se nao der erro...
            return n # retorne o valor n, que foi o digitado.



#programa principal
n1 = leiaint('Digite um valor Inteiro: ')
n2 = leiafloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor Real foi {n2}')