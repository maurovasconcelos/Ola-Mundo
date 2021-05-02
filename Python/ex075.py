num = (int(input('Digite um número: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valoeres {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
for n in num:
        if n % 2 ==0:
                print(n, end= ' ')