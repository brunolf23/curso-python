'''for c in range (0, 100, 3):
    print (c)

----------------------------------

soma = 0
for nome in range (0, 4):
    n = int(input('Digite um valor: '))
    soma = soma + n
print (f'O somatório de todos os valores foi {soma}.')

----------------------------------

n = int(input('Digite um número: '))    
for nome in range (0, n + 1):
    print (nome)
print ('FIM!')'''


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print (c)
print ('FIM')