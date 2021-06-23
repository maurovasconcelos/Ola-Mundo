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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[33m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ') #retorne o que foi diigtado, Ex: 1,2,3,4
    return opc

