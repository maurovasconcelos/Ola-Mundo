from datetime import date
ano = int(input('Que ano deseja analizar? '))
if ano == 0:
    ano = date.today().year  #Comando pra ver a data atual da sua maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:  #Se o resto do ano dividido por 4  for 0, ou o resto do ano/100 for diferente de 0 ou ano/400 for 0, faça // formula utilizada pra se negoçar o ano bisexto
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} NÂO é bissexto'.format(ano))
