resp = 'S'
media = soma = quant = maior = menor = 0 #todas as variavies com o valor 0 podem ser póstas dessa maneira
while resp in 'Ss': # se a resposta for igual a 'Ss', faça:
    num = int(input('digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num # se a quantidade for igual a 1 o maior e o menos vao receber o valor do numero
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0] # joga pra maiusculo e tira espaços ->[0] pra considerar só a primeira letra
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
