# Classificando Atletas

from datetime import date
data = int(input('Ano de nascimento: '))

atual = date.today().year
idade = atual - data

if idade <= 9:
    print (f'Você tem {idade} ano(s), está na categoria MIRIM.')
    
elif idade <= 14:
    print (f'Você tem {idade} ano(s), está na categoria INFANTIL.')
    
elif idade <= 19:
    print (f'Você tem {idade} ano(s), está na categoria JUNIOR.')
    
elif idade <= 25:
    print (f'Você tem {idade} ano(s), está na categoria SêNIOR.')
    
else:
    print (f'Você tem {idade} ano(s), está na categoria MASTER.')