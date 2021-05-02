valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.') # vc digitou tantos elementos
valores.sort(reverse=True) #pelamor de deus ne
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O numero 5 está dentro dos valores...')
else:
    print('O numero 5 não está dentro dos valores...')