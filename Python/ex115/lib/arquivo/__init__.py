from ex115.lib.interface import *

def arqExiste(nome): # verificando se o arquvivo existe
    try:
        a = open(nome, 'rt') # a vai abrir  e verificar se exist eo arquivo e rt =  leitura de arquivo texto
        a.close()
    except FileNotFoundError: # se o arquivo não for encontrado, retorne o valor Falso
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+') # cria um arquivo 'wt'  = Whrite e o +, = gravação de arquivo de texto
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo! ')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # formatação bonitinha, alinhar nomes a esquerda e idades a direita
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na avertuda do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()