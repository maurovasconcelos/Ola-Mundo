from math import hypot
co = float(input('Comprimeito do cateto oposto: '))
ca = float(input('Comptumeito do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))