N = int(input('Quantos alunos? '))

students = {}

for i in range(1, N+1):
  name = input(f'Nome do aluno {i}: ')
  notas = []

  for j in range(1, 5):
    nota = float(input(f'{j}ª Nota do aluno {name}: '))
    notas.append(nota)

  students[name] = notas

for name, notas in students.items():
  average = sum(notas) / len(notas)
  result = 'aprovado' if average >= 7.0 else 'reprovado'
  print(f'O aluno {name} foi {result} com média {average:.1f}')
