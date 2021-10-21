from time import sleep
from ex108 import moeda
p = float(input('Digite o preço: R$'))
print('-=' * 20)
print('CALCULANDO...')
print('-=' * 20)
sleep(2)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
sleep(2)
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
sleep(2)
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
sleep(2)
print(f'Diminuindo em 20%, temos {moeda.moeda(moeda.diminuir(p, 20))}')
