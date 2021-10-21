from datetime import date
ano = int(input('Que ano quer analisar? Coloque''\033[36m'' 0 ''\033[m''para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é''\033[31m'' BISSEXTO! ''\033[m'.format('\033[33m', ano, '\033[m'))
else:
    print('O ano {}{}{} NÃO é''\033[31m'' BISSEXTO! ''\033[m'.format('\033[33m', ano, '\033[m'))
