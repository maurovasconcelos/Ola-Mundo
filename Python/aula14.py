n = 1
par = 0
impar = 0
while n != 0: # se o numero 'n' for diferente ' != ' de 0, faça: se o n resto 2 = 0: par recebe +1
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print('Você digitou {} némeros pares e {} números impares!'.format(par, impar))