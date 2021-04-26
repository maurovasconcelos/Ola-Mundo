frase = str(input('Digite uma frase: ')).strip().upper() #frase sem espaços e lida como se estivesse toda em maiusculo, o upper
palavras = frase.split()# splitou a frase pra gerar uma lista
junto = ''.join(palavras) #juntei a lista pra eliminar espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1): # fiz o inverso, trocando da ultima letra ate a primeira
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')