#

numero = int(input('Digite um número: '))

for i in range (1, numero + 1):
    if numero % i == 0:
        print ('\033[34m', end=' ')
    else:
        print ('\033[33m', end=' ')
    print (f'{i}', end=' ')