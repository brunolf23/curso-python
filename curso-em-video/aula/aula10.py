n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

calculo = (n1 + n2) / 2

print (f'A sua média foi {calculo:.1f}')

if calculo >= 6.0:
    print (f'Você está aprovado.')
else:
    print (f'Você está reprovado.')