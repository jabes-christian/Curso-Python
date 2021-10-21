from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
ida = atual - nasc
print('O atleta tem {} anos.'.format(ida))
if ida <= 9:
    print('Classificação: MIRIM')
elif ida <= 14:
    print('Classificação: INFANTIL')
elif ida <= 19:
    print('Classificação: JÚNIOR')
elif ida <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
