cid = str(input('Em qual cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

print('-'*30)

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


