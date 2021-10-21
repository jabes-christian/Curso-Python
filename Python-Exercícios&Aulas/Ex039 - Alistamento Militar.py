from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
sexo = str(input('Qual é o seu sexo: '))
ida = atual - ano
if sexo == 'masculino':
    print('De acordo com o Estado você TEM A NECESSIDADE de se ALISTAR!')
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, ida, atual))
    if ida == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif ida < 18:
        sal = 18 - ida
        dat = ano + sal
        print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(sal, dat))
    elif ida > 18:
        sal = ida - 18
        dat = ano + sal
        print('Você deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(sal, dat))
else:
    print('De acordo com Estado você NÃO TEM A NECESSIDADE de ALISTAR!')
