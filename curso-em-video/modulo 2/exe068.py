# Jogo do Par ou Ímpar

import random

print ('-=' *25)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('-=' *25)

while True:
    numero_aleatorio = random.randint(1, 100)
    numero = int(input('Digite um valor: '))
    resultado = numero_aleatorio + numero
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar: [P/I] ')).upper()
        if escolha == 'P':
            print (f'par {resultado}')
        elif escolha == 'I':
            print (f'impar {resultado}')
    