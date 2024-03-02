# Analisador completo

soma_idade = 0
media_idade = 0
maior_idade = 0
nome_velho = ''
mulher_anos = 0

for p in range (1, 5):
    print (f'======== {p}ª ========')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: '))
    soma_idade += idade
    
    if p == 1 and sexo == 'Mm':
        maior_idade = idade
        nome_velho = nome
        
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
        
    if sexo in 'Ff' and idade < 20:
        mulher_anos += 1
    
media_idade = soma_idade / 4
print (f'A media de idade é {media_idade}')
print (f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}.')
print (f'Ao todo são {mulher_anos} mulheres com menos de 20 anos.')