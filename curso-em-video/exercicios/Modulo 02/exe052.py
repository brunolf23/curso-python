# Números primos

numero = int(input('Digite um número: '))
contador = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        print ('\033[33m', end=' ')
        contador +=1
    else:
        print ('\033[32m', end=' ')
    print (f'{i}', end=' ')
    
print (f'\n O número {numero} foi divisível {contador} vezez.')