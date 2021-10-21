n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('Soma entre os valores gigitados é'.format(s))
print(f'Soma entre os valores digitados é {s}')