n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end=' ')
print ('Divisao inteira {} e potencia {}'.format(di, e))