num = int(input('digite um numero inteiro: '))
print('''Escolha uma das basese para a conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converver para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} Convertido para BINARARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print(f'{num} Convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opção invalida, tente novamente ')

#revisado
