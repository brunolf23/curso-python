# Progressão Aritmética

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão'))
n = termo + (10 - 1) * razao

for i in range (termo, n + 1, razao):
    print (f'{i}', end=" => ")
print ('ACABOU')