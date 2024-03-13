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
        escolha = str(input('Par ou Ímpar: [P/I] ')).upper().strip()
        if escolha == 'P':
            if resultado % 2 == 0:
                print (f'Você venceu {resultado}')
                contador += 1
            else:
                print ('Você perdeu!')
                break
        elif escolha == 'I':
            if resultado % 2 == 1:
                print (f'Você venceu! {resultado}')
                contador += 1
            else:
                print ('Voce perdeu')
                break
        print ('Vamos jogar novamente?')
    print (f'GAME OVER! Você venceu {contador} vezes.')
    