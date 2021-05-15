aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:# se o aluno na chave media for >= 7
    aluno['situação'] = 'Aprovado' # sua chave situação recebe o valor 'Aprovado'
elif 5 <= aluno['media'] < 7 : # se estiver entre 5 e 7 a key situação recebe recuperação
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items(): # pra cada chave nos valores faça:
    print(f'{k} é igual a {v}') # me mostre a chave=nome que é igual ao valor=nome