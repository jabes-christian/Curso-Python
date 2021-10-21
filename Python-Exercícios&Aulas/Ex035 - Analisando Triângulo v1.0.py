print('\033[33m''-=-''\033[m'*15)
print('\033[34m''Analisador de Triângulos''\033[m')
print('\033[33m''-=-''\033[m'*15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima''\033[31m'' PODEM FORMAR ''\033[m''triângulos!')
else:
    print('Os segmentos acima''\033[31m'' NÃO PODEM FORMAR''\033[m'' triângulos!')
