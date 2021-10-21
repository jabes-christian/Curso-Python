larg = float(input('Largura da Parede = '))
alt = float(input('Altura da parede = '))
a = larg * alt
lit = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(larg, alt, a))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(lit))


