# Média das Notas

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) /2


if media < 5.0:
    print (f'Sua nota foi {media}. Você foi REPROVADO.')
    
elif 7 > media >= 5:
    print (f'Sua nota foi {media}. Você está de RECUPERAÇÃO.')
    
elif media >= 7.0:
    print (f'Sua nota foi {media}. Você está APROVADO.')