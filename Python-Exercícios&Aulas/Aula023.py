try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informa os dados!')
else:
    print(f'O resultado da divisão é {r:.2f}')
finally:
    print('VOLTE SEMPRE! MUITO OBRIGADO')
