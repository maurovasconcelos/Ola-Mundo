area = [] #area é uma lista
def area(lar, comp): #função area vai receber 2 valores,que vão se tornar largura e comprimento,
    a = lar * comp # a variavel a/area é igual a multiplicação dos 2 valores
    print('A area da um terreno {}x{} é igual a {}m² '.format(l, c, a))# print basico
#---Aqui que começa

l = float(input('Largura do Terreno (m): '))
c = float(input('Comprimento do Terreno (m): '))
area(l, c)#chamando a função área, lar e comp recebem o os valoers de l e c



