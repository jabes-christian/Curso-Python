times = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'>>> Quantos gols na {c+1} partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Por favor digite somente (S) ou (N)')
    if resp == 'N':
        break
    print('=-' * 30)
print('=-' * 30)
print(f'{"cod":<4}{"nome":<20}{"gols":<20}{"total":<2}')
print('-' * 50)
for k, v in enumerate(times):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para interromper): '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERROR! Não existe jogador com código {busca}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {times[busca]["nome"]}')
        for i, g in enumerate(times[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('=-' * 25)
print('<<< Volte Sempre >>>')

