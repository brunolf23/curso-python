velocidade = int(input('Qual a velocidade do carro? '))

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print (f'Parabéns, você está a {velocidade}Km/h, limite de velocidade permitido.')
else:
    print (f'Você estava a {velocidade}Km/h, por isso foi multado.')
    print (f'Você tera que pagar {multa}')
    
    '''if velocidade > 80:
        print ('Multado!')
        multa = (velocidade - 80) * 7
        print (f'Você deve pagar, uma multa de R$ {multa}')'''