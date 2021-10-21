n = float(input('Uma distância em metros = '))
c = n / 1000
h = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n, c, h, dam, dm, cm, mm))
