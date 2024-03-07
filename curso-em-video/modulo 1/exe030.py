# Par ou Ímpar?

numero = int(input('Digite um número para saber se é par ou ímpar: '))
calcular = numero % 2

if calcular == 0:
    print (f'O número {numero} é par.')
else:
    print (f'O número {numero} é ímpar.')