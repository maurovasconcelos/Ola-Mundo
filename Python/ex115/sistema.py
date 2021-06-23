from ex115.lib.interface import * # import * = import tudo
from ex115.lib.arquivo import *
from time import sleep
from pygame import mixer
arq = 'cursoemvideo.txt'

if not arqExiste(arq): #Se o arquivo nao esxistir, ele cria
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Birijhonson', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar a garelinha
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3: # falhou, falta melhorar a parte da musiquinha
        mixer.init()
        mixer.music.load('giornosax.mp3')
        mixer.music.play()
    elif resposta == 4:
        cabeçalho('\033[34mSaindo do sistema... Até logo!\033[m')
        break
    else:
        cabeçalho('ERRO! Digite uma opção válida!')
    sleep(1)
