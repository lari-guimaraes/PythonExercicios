import math

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjascente: '))
hip = math.hypot(op, ad)
print('O comprimento da hipotenusa é de {:.3f}!'.format(hip))
