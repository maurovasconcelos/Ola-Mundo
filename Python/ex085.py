lista = [[], []] # sim... uma lista com 2 listas
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)# se o resto do valor dividido por 2 for igual a 0, a lista [0]'par' recebe o valor
    else:
        lista[1].append(valor) # senao, a lista [1]'impar' vai receber o valor
print('-=' * 30)
lista[0].sort() # ordem crescente
lista[1].sort()
print(f'Os valores PARES digitados foram: {lista[0]}')
print(f'Os valores IMPARES digitados foram: {lista[1]}')