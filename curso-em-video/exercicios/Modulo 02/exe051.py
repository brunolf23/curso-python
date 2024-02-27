# Progressão Aritmética

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range (termo, 10, razao):
    print (f'{i}', end=" => ")
print ('ACABOU')