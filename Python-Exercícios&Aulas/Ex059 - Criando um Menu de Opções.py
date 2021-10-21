v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa''')
    opc = int(input('>>> Qual é a sua opção? '))
    if opc == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, soma))
    elif opc == 2:
        multiplicaçao = v1 * v2
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, multiplicaçao))
    elif opc == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
            print('Entre {} e {} o maior é {}'.format(v1, v2, maior))
    elif opc == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente!')
    print('=-='*12)
print('Fim do programa, Volte sempre!')
