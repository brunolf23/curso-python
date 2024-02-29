# Interrompendo repetição while

'''cont = 1 # apenas para ter um início no meu while
while cont <= 10:
    print (cont, ' ', end='-> ')
    cont += 1
print ('ACABOU')'''

# ---------------------------------------

numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print (f'A soma vale {soma}')