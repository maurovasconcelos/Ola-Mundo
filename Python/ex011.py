larg = float(input('A largura da parece: '))
alt = float(input('Altura da parece: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m²'.format(larg, alt, area))
tinta = area / 2
print('Para printar essa parece, você precisara de {}l de tinta'.format(tinta))

