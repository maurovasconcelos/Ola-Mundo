lanche = ('Hambúruer', 'Suco', 'Pizza','Pudin', 'Batata Frita' )


# pra cada item na lista de lanches, posso pesquisar por indice
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:        # pra cada comida em lanche, vou printar toda a lista
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):      # pra cada posição e comida na lista enumerate(lanche), vou mostrar toda a lista com cada item na sua posição
    print(f'Eu vou comer {comida} na posição {pos}')

    #formas de fazer tuplas
    #basicamente a mesma coisa, porem de maneiras diferentes de se fazer


print('Nuuu, comi ')