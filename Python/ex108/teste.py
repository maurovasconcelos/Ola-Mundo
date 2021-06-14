import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de R$:{moeda.moeda(p)} é R$:{moeda.moeda(moeda.metade(p))}') #primeiro meda = nome do modulo, segundo moeda = função, terceiro moeda = nome do parametro
print(f'O dobro de R$:{moeda.moeda(p)} é R$:{(moeda.moeda(moeda.dobro(p)))}')
print(f'Aumentando 10%, temos R$:{moeda.moeda(moeda.aumentar(p, 10))}')
print(f'R$:{p}, menos 25%, temos R$:{moeda.moeda(moeda.diminuir(p, 25))}')