

#-----------------------------------------------------------------------------------------------------------------------
def somar(a=0,b=0,c=0):
    """
    -> faz a soma de 3 valores e mostra o resultado
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """


    s = a + b + c
    return s


r1 = somar(3,2,5)
r2 = somar(3,2)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}')