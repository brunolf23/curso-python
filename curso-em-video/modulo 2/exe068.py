# Jogo do Par ou Ímpar

import random

print ('-=' *25)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('-=' *25)

lista = [0, 999]
computador = random(lista)
while True:
    numero = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar: [P/I] ')).upper()