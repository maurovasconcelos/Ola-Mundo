a = int(input('Escreva o primeiro numero: '))
b = int(input('Escreva o segundo numero: '))
c = int(input('Escreva o terceiro numero: '))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O MENOR valor foi {}'.format(menor))
print('O MAIOR valor foi {}'.format(maior))


