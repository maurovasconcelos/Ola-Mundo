num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m',end='') #codigo cor azul, os que ficarem azul sao divisivel
        tot =+ 1
    else:
        print('\033[31m', end='') #codigo cor vermelha, os que nao foram divisiveis ficam amarelos
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes '.format(num, tot)) # \n\033[m é o codigo pra quebrar e zerar a cor
if tot == 2:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÂO È PRIMO!')