nome = str(input('Digite seu nome: '))
if nome == 'Mauro':
    print('Que nome lindo !')
elif nome == 'Pedro' or nome == 'Alex' or nome == 'Fulano':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))