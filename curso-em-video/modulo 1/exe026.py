# Primeira e última ocorrência de uma string

letra = str(input('Digite uma frase: ')).upper().strip()

print (f'A letra A aparece {letra.count('A')} vezes na frase.')
print (f'A primeira letra A apareceu na posição {letra.find('A')+1}')
print (f'A última letra A apareceu na posição {letra.rfind('A')+1}')