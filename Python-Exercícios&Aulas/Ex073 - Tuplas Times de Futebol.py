times = ('Forteza', 'Athlético-PR', 'Atlético-GO', 'Bragantino',
        'Bahia', 'Fluminense', 'Palmeiras', 'Flamengo',
        'Atlético-MG', 'Corinthians', 'Ceará SC', 'Santos',
        'Cuiabá', 'Sport', 'São Paulo', 'Juventude',
        'Internacional', 'Gremio', 'América-MG', 'Chapecoense')
print('-='*20)
print(f'Lista de times {times}')
print('-='*20)
print(f'Os 5 primeros são {times[0:5]}')
print('-='*20)
print(f'Os últimos 4 colocados {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
