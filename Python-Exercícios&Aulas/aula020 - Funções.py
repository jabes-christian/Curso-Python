# Parte 01 - EX 01
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')


# PROGRAMA PRINCIPAL
soma(4, 5)
soma(b=8, a=9)
soma(2, 1)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(1, 3, 5)
soma(2, 8)
soma(8, 3)


# EX 02
def contador(*num):
    for valor in num:
        print(f'{valor}', end='')
    print(' FIM')
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números')


contador(2, 3, 4, 5)
contador(1, 6, 2)
contador(8, 6, 3, 7, 9, 10)

#EX 03
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 5, 4, 8]
dobra(valores)
print(valores)

# Parte 02 - EX 01


def contador(i, f, p):
    """
    -> Faz uma contagem e demonstra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    print('-=' * 20)
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)
contador(1, 20, 3)
contador(0, 100, 10)

# EX 02


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra na tela!
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print('-=' * 20)
    print(f'A soma dos valores será {s}')

help(somar)
somar(2, 6, 8)
somar(2, 5)

# EX 03


def função(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A) dentro vale {a}')
    print(f'B) dentro vale {b}')
    print(f'C) dentro vale {c}')

a = 5
função(a)
print(f'A) fora vale {a}')

# EX 04


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(2, 3, 8)
r2 = somar(5, 3)
r3 = somar(4)
print(f'A soma entre os valores será {r1}, {r2}, {r3}')

# EX 05


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return  f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(2)
print(f'Os resultados serão {f1}, {f2}, {f3}')

# EX 06


def par(n=0):
    if n% 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(par(n))
