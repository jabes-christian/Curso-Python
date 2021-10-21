# Testando dicionários
'''pessoas = {'nome': 'Jabes', 'sexo': 'Masculino', 'idade': 18}
print(f'Seu nome é: {pessoas["nome"]}\n'
      f'Você é do Sexo: {pessoas["sexo"]}\n'
      f'Sua Idade é de: {pessoas["idade"]} anos ')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Bernardo'
pessoas['peso'] = 80.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# Criando Dicionário dentro de uma lista
'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

# Ex
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    print('-=' * 20)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
