from time import sleep
from ex109 import moeda
p = float(input('Digite o preço: R$'))
print('-=' * 20)
print('CALCULANDO...')
print('-=' * 20)
sleep(2)
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
sleep(2)
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
sleep(2)
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
sleep(2)
print(f'Diminuindo em 13%, temos {moeda.diminuir(p, 13, True)}')
