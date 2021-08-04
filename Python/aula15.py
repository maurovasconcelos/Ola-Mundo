n = s = cont = 0
while True:  # enquanto isso for verdade repita:
    n = input('Digite um numero: ')
    cont += 1
    if not n.isnumeric():
        print('Digite um nome válido !')
    elif n == 999:
        cont -= 1
        break
    s += n # soma é soma + o numero
#print('A soma vale {}'.format(s))

print(f'A soma vale {s}, e você digitou {cont} numeros') # neeeeeem fodendo,e eu usando .format a 65 exercicios!!