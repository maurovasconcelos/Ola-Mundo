


def voto(ano):
    from datetime import date # da pra usar importações dentro de funçoes, economiza memoria e é mais pika
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f'Com {idade} anos: NÂO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        return  (f' Com {idade} anos: VOTO OPCIONAL.')
    else:
        return (f'Com {idade} anos: VOTO OBRIGATORIO!')

#programa principal
nasc = int(input('Em que ano você nasceu ? '))
print(voto(nasc))
