not1 = float(input('Qual foi sua primeira nota: '))
not2 = float(input('Qual foi sua segunda nota: '))
media = (not1 + not2) / 2
if media >=5 and media < 7:
    print('Sua média total é {} e você esta de RECUPERAÇÂO!'.format(media))
elif media < 5:
    print('Sua média foi {} e você foi REPROVADO!'.format(media))
else:
    print('Sua média foi {} e você foi APROVADO!'.format(media))
