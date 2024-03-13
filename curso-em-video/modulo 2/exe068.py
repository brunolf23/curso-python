# Jogo do Par ou Ímpar

import random

print ('-=' *25)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('-=' *25)

contador = 0

while True:
    numero = int(input('Digite um valor: '))
    numero_aleatorio = random.randint(1, 100)
    resultado = numero_aleatorio + numero
    escolha = ' '
    
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar: [P/I] ')).upper()[0].strip()
    if escolha == 'P':
        if resultado % 2 == 0:
            print (f'Você venceu! {resultado} é par.')
            contador += 1
        else:
            print (f'Você perdeu, {resultado} é ímpar.')
            break
        
    elif escolha == 'I':
        if resultado % 2 == 1:
            print (f'Você venceu! {resultado} é ímpar.')
            contador += 1
        else:
            print (f'Voce perdeu, {resultado} é par.')
            break
    print ('Vamos jogar novamente?\n')

print (f'GAME OVER! Você venceu {contador} vez(es).\n')