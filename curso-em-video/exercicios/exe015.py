dias = int(input('Quantos dias alugados? '))
distancia = float(input('Quantos km rodados? '))

diaria = (dias * 60) + (distancia * 0.15)

print('A diaria por 60,00 e o valor de cada km rodado 0,15.')
print(f'{dias} dias e {distancia}km rodados.')
print(f'O total a pagar é R${diaria:.2f}')