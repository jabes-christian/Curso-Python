v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('\033[31m''MULTADO! Você excedeu o limite permitido que é de 80km/h')
    mul = (v-80) * 7
    print('\033[31m''Você deve pagar uma multa de {}R${:.2f}{}!''\033[m'.format('\033[33m', mul,'\033[m'))
print('\033[32m''Tenha um bom dia! Dirija com segurança!''\033[m')
