a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o MENOR!
'''if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c'''
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o MAIOR!
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[31m''O menor valor digitado foi: {}{}{}''\033[m'.format('\033[33m', menor, '\033[m'))
print('\033[31m''O maior valor digitado foi: {}{}{}''\033[m'.format('\033[33m', maior, '\033[m'))
