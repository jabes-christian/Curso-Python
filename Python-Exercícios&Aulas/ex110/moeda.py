def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    from time import sleep
    print('-=' * 20)
    print('RESUMO DO VALOR'.center(30))
    print('-=' * 20)
    sleep(2)
    print(f'Analisando preços: \t\t{moeda(preço)}')
    sleep(1)
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    sleep(1)
    print(f'Metade do preço: \t\t{metade(preço, True)}')
    sleep(1)
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    sleep(1)
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-=' * 20)