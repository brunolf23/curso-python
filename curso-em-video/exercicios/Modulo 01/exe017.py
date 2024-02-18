# Catetos e Hipotenusa

from math import hypot

opo = float(input('Qual o comprimento do cateto oposto? '))
adj = float(input('Qual o comprimento do cateto adjacente? '))

cate = hypot(opo, adj)

print(f'A hipotenusa vai medir {cate:.2f}')
