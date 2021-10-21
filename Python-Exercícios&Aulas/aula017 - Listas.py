'''# Ex 01
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(3, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista têm {len(num)} elementos')'''

# Ex 02
'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei no final da lista!')'''

# Ex 03
'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')'''

# Listas( Part 2 ) Ex01
'''teste = list()
teste.append('Jabes')
teste.append(18)
galera = list()
galera.append(teste[:])
teste[0] = 'Emilly'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

# Ex02
'''galera = [['João', 18], ['Ana', 23], ['Matheus', 25], ['Maria', 28]]
print(galera[0][1])
print(galera[2][1])
print(galera[3][0])
print(galera[1][0])'''

#Ex03
galera = list()
dado = list()
totmai = totmen = 0
for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')

