num = 0  # ou num = cont = 0, pois todas as variveis recebem 0 
cont = 0
soma = 0
num = int(input('Digite um número [999 Para parar]: '))
while num != 999:
    soma += num #soma recebe soma mais numero
    cont += 1 # contador recebe ele mais 1
    num = int(input('Digite um número [999 Para parar]: '))
print('Você digitou {} numeros, e a soma entre eles foi {}'.format(cont,soma))