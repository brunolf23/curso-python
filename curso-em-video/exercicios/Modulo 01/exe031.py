viagem = float(input('Qual a distância da viagem em Km? '))

if viagem <= 200:
    pass1 = viagem * 0.50
    
else:
    pass1 = viagem * 0.45

print (f'O preço da sua viagem será de R${pass1:.2f}')