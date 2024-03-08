# Progressão Aritmética v.2.0

print ('Gerador de PA')
print ('-=' * 10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = termo
cont = 1

while cont <= 10:
    print (f'{termo} -> ', end='')
    termo += razao
    cont += 1
print ('FIM!')