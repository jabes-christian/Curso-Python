def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número:
    :param num: Um número a ser calculado.
    :param show: (opcional) Mostra ou não a resolução do resultado
    :return: O valor de um Fatorial de um número (num)
    """
    f = 1
    print('-=' * 20)
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
help(fatorial)
n = int(input('Digite um Número: '))
print(f'{fatorial(n, show=True)}')
print(f'O fatorial de {n} é igual a {fatorial(n)}')
