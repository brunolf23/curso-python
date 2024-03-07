# Índice de Massa Corporal

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print (f'Seu IMC é {imc:.1f}. Abaixo do peso')
    
elif 18.5 <= imc < 25:
    print (f'Seu IMC é {imc:.1f}. Peso ideal.')
    
elif 25 <= imc < 30:
    print (f'Seu IMC é {imc:.1f}. Sobrepeso.')
    
elif 30 <= imc < 40:
    print (f'Seu IMC é {imc:.1f}. Obesidade.')
    
else:
    print (f'Seu IMC é {imc:.1f}. Obesidade mórbida, cuidado!')