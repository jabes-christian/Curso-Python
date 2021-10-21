from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} têm o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} têm o COSSENO de {:.2f}'.format(ang, coss))
print('O ângulo de {} têm a TANGENTE de {:.2f}'.format(ang, tang))




