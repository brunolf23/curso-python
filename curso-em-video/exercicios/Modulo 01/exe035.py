r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os comprimentos acima formam um triângulo')
else:
    print ('OS comprimentos acima não formam um triângulo')