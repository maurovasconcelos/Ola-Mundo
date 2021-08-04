r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 ==r3:
        print('EQUILATEDO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÒSCELES')
else:
    print('Os segmentos acima NÂO PODEM FORMAR um triangulo')

#mesma coisa do exercico do triangulo anterior, porem agora mostra se é equilatero, escaleno e etc...