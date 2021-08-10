while True:
    n = int(input('Quer ver a tabuada de que número: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')

    print('-' * 30)
print('Programa de tabuada encerrado !')