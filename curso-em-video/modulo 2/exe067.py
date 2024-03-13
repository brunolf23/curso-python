# Tabuada v.3.0

while True:
    escolha = int(input('Quer ver a tabuada de qual valor? '))
    print ('-' * 30)
    if escolha < 0:
        break
    for numero in range (1, 11):
        print (f'{escolha} x {numero:2} = {escolha * numero:2}')
    print ('-' * 30)
print ('TABUADA ENCERRADA.')