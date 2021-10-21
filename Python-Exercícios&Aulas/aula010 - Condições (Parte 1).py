#nome = str(input('Qual é o seu nome? '))
#if nome == 'Jabes':
#    print('Que lindo nome você tem!')
#else:
#    print('Seu nome e tão normal!')
#print('Bom dia, {}!'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua media foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
