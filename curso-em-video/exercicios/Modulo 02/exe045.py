# Pedra, Papel e Tesoura

from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
sortear = randint(0, 2)

print ('''Suas opções:
       [0] Pedra
       [1] Papel
       [2] Tesoura''')

jogada = int(input('Qual é a sua jogada? '))

print ('-=' * 15)
print (f'Computador jogou {lista[sortear]}')
print (f'Jogador jogou {lista[jogada]}')
print ('-=' * 15)

if sortear == 0:
    if jogada == 0:
        print ('EMPATE')
        
    elif jogada == 1:
        print ('JOGADOR VENCE')
        
    elif jogada == 2:
        print ('COMPUTADOR VENCE')
        
elif sortear == 1:
    if jogada == 0:
        print ('COMPUTADOR VENCE')
        
    elif jogada == 1:
        print ('EMPATE')
        
    elif jogada == 2:
        print ('JOGADOR VENCE')
    
elif sortear == 2:
    if jogada == 0:
        print ('JOGADOR VENCE')
        
    elif jogada == 1:
        print ('COMPUTADOR VENCE')
        
    elif jogada == 2:
        print ('EMPATE')