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
    print('{} Convertido para {} é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente ')
