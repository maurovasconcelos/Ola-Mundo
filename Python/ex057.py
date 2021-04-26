sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # comand[0] é pra ler apenas a primeira letra, pra quando a pessoa digitar Marculino, ler só o M
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sicesso'.format(sexo))