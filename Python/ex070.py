total = 0
tot1000 = 0
menor = 0
cont = 0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    preço = float(input('Qual o preço do produto R$: '))
    cont += 1
    total += preço
    if preço > 1000:
        tot1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA! '))
print(f'O total da compra foi {total:.2f}')
print(f'Foram {tot1000} produtos acima de 1000 reais.')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
