#num_int = input('Digite um número inteiro: ')

#if num_int.isdigit():
 #   num_int = int(num_int)
  #  if num_int %2 == 0:
   #     print(f'{num_int} é PAR')
    #else:
     #   print(f'{num_int} é IMPAR')
#else:
#    print(f'{num_int} não é um numero inteiro')



"""horario = input('Digite um horario: ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario deve estar entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde !')
        else:
            print('Boa noite!')


else:
    print('Por favor digite um horario entre 0 e 23.')"""

#-------------------------------------------------------------------------------------------------


nome = input('Digite seu nome: ')
if nome.isalpha():
    tamanho = len(nome)

    if tamanho <= 4:
        print('Seu nome é curto')
    elif tamanho <= 6:
        print('seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Digite um nome valido')