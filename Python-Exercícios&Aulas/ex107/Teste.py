from time import sleep
import moeda
p = float(input('Digite o preço: R$'))
print('-=' * 20)
print('CALCULANDO...')
print('-=' * 20)
sleep(2)
print(f'A metade de {p} é {moeda.metade(p)}')
sleep(2)
print(f'O dobro de {p} é {moeda.dobro(p)}')
sleep(2)
print(f'Aumentando em 10%, temos R${moeda.aumentar(p, 10)}')
sleep(2)
print(f'Diminuindo em 20%, temos R${moeda.diminuir(p, 20)}')
