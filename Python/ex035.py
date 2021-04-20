print ('-=-'*20)
print('Analizador de triangulos')
print('-=-'*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float (input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  #formular dos triangulos, onde um nao pode ser maior que os outros dois lados
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acime NÂO PODEM FORMAR um triangulo!')