# Analisando Triângulos v.2.0

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos acima podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print ('EQUILÁTERO!')
    
    elif r1 != r2 != r3 != r1:
        print ('ESCALENO!')
        
    else:
        print ('ISÓSCELES!')

else:
    print ('Os segmentos acima não podem formar um triângulo.')