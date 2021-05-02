lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: # se o c for igual a zero OU o numero for maior que o ultimo valor insira o numero /append(n)
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 # posição começa com 0
        while pos < len(lista): # Enquanto a posição for menor que o len de lista // ele vai da posição 0 até a ultima posição
            if n <= lista[pos]:
                lista. insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=-' * 30)
print(f'Os valores digitador em ordem foram {lista}')