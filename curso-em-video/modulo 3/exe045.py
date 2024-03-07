# Pedra, Papel e Tesoura

from random import randint

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
        
        
'''from random import randint

opcoes = ['Pedra', 'Papel', 'Tesoura']

print('Suas opções:')
for i, op in enumerate(opcoes):
    print(f'[{i}] {op}')

escolha_jogador = int(input('Qual é a sua jogada? '))
escolha_computador = randint(0, 2)

print('-=' * 15)
print(f'O computador escolheu {opcoes[escolha_computador]}')
print(f'O jogador escolheu {opcoes[escolha_jogador]}')
print('-=' * 15)

resultado = (escolha_jogador - escolha_computador) % 3

if resultado == 0:
    print('EMPATE')
elif resultado == 1:
    print('O JOGADOR VENCE')
else:
    print('O COMPUTADOR VENCE')'''
