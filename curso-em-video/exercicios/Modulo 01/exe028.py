# Jogo da Adiovinhação v.1.0

from random import randint
from time import sleep

print ('-=-' * 20)
print ('Vou pensar em um número de 0 a 5. Tenten adivinhar...')
print ('-=-' * 20)

numero = int(input('Em que número eu pensei? '))
lista = randint(0, 5)

print ('Processando...')
sleep(2)

if numero == lista:
    print ('Parabéns, você acertou!')
else:
    print (f'Errou! O número que eu pensei foi o {lista}.')