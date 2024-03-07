# Jogo da Adivinhação v.2.0

from random import randint

print ('-=-' *20)
print ('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print ('-=-' *20)

numero = int(input('Em que número pensei? '))
lista = randint(0, 10)
cont = 1

while numero != lista:
    print (f'Errou! O número que eu pensei foi o {lista:2}.')
    numero = int(input('Tente novamente: '))
    lista = randint(0, 10)
    cont += 1
print (f'Parabéns, você acertou!\nForam {cont} palpite(s)!')