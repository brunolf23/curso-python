lar = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))

area = lar * alt
tinta = area
tinta = area / 2

print(f'A sua parede tem dimensão de {lar} x {alt} a sua área é de {area:.1f}m².')
print(f'Então sera necessário gastar {tinta:.1f} litros de tinta.')