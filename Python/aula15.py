n = s = cont = 0
while True: # enquanto isso for verdade repita:
    n = int(input('Digite um numero: '))
    cont += 1
    if n == 999: # se o numero for igual a 999 interrompa
        cont -= 1
        break
    s += n # soma é soma + o numero
#print('A soma vale {}'.format(s))

print(f'A soma vale {s}, e você digitou {cont} numeros') # neeeeeem fodendo,e eu usando .format a 65 exercicios!!