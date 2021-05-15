def titulo(txt):
    print('-=' * 30)
    print(txt)

#programa principal
titulo('   APRENDENDO PYTHON    ')
titulo('  PYTHON É MUITO BOM !  ')
titulo('Oi')

#-----------------------------------------------------------------------------------------------------------------------

def soma(* valores): #a função soma vai receber altos valores
    s = 0 #soma =0
    for num in valores: # pra cada numero em valores faça:
        s += num #soma recebe ela + o numero
    print('Somando os valores {} temos {}'.format(valores, s))


soma(5, 2)
soma(2, 8, 4)                         #fragou?

#-----------------------------------------------------------------------------------------------------------------------
valores = []
def dobra(lista):
    pos = 0 # contador
    while pos < len(lista): # se a posição da do item tal da lista for menor que o tamanho da lista faça o numero da posiçao *2
        lista[pos] *= 2 # posição 1 da lista recebe ela*2
        pos += 1 # contador pos  sobe +1 pra pra executar na proxima posição

valores = [6, 3, 9, 1, 9, 2]
print(valores)
dobra(valores)  # chamando a função dobra, que adivinha...
print(valores)