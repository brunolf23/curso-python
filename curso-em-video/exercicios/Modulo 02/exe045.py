# Pedra, Papel e Tesoura

from random import choice

print ('''Suas opções:
       [1] Pedra
       [2] Papel
       [3] Tesoura''')

jogada = int(input('Qual é a sua jogada? '))

lista = [1, 2, 3]
sortear = choice(lista)

if jogada == 1: