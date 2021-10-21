nome = str(input('Qual é o seu nome? '))
if nome == 'Jabes':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Gustavo' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Juliana Ana Cláudia Lara':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tem um bom dia, {}!'.format(nome))
