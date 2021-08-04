def somar(a=0,b=0,c=0):
    s = a + b + c
    return s
r1 = somar(3,5,9)
r2 = somar(5,8)
r3 = somar(12,1)

print(f'Os resultados foram {r1}, {r2} e {r3}')
print('-=' * 30)
#-----------------------------------------------------------------------------------------------------------------------
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

# ---------------------------------------------------------------------------------------------------------
num = [6, 2, 1, 4, 3]
num.sort()

#----------------------------------------------------------------------------------------------------------
N = int(input('Quantos alunos? '))

students = {}

for i in range(1, N+1):
  name = input(f'Nome do aluno {i}: ')
  grades = []

  for j in range(1, 5):
    grade = float(input(f'Nota {j} do aluno {name}: '))
    grades.append(grade)

  students[name] = grades

for name, grades in students.items():
  average = sum(grades) / len(grades)
  result = 'aprovado' if average >= 7.0 else 'reprovado'
  print(f'O aluno {name} foi {result} com média {average:.1f}')
