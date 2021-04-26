soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 ==0: # se resto do numero %2 for igual a 0, faça:
        soma += num #soma recebe soma + num
        cont += 1 # conta recebe cont +1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))