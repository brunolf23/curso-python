# Grupo da Maioridade

import datetime

atual = datetime.date.today().year
total_menor = 0
total_maior = 0

for i in range (1, 8):
    nascimento = int(input(f'Digite o ano do {i}ª nascimento: '))
    idade = atual - nascimento

    if idade <= 18:
        total_menor += 1
    else:
        total_maior += 1
        
print (f'{total_menor}, pessoa(s) que ainda não atingiu a maior idade.')
print (f'{total_maior}, pessoas(s) que já atingiu a maior idade.')