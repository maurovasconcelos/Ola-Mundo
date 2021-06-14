def leiadinheiro(msg):
    valido = False
    while not valido: # enquanto nao for valido, faça
        entrada = str(input(msg)).replace(',', '.') # vai ler em string pra poder tratar a string
        if entrada.isalpha() or entrada.strip() == '': # se essa entrada for alfanumerico , vai da erro
            print(f'ERRO: \"{entrada}\" é um preço inválido')
        else:
            valido = True
            return float(entrada)