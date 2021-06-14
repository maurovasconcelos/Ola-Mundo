from ex109 import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de R$:{moeda.moeda(p)} é {moeda.metade(p, True)}') # p = primeiro parametro, True = esta formatado? True, ai o resultado ja tem formatado
print(f'O dobro de R$:{moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'R$:{p}, menos 25%, temos {moeda.diminuir(p, 25, True)}')