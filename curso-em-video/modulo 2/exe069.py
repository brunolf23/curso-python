# Análise de dados do grupo

contador_idade = 0
contador_homem = 0
contador_mulher = 0

while True:
    print ('-=' *20)
    print ('CADASTRE UMA PESSOA')
    print ('-=' *20)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    opcao = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).upper()[0].strip()
    if idade >= 18:
        contador_idade += 1
    if sexo == 'M':
        contador_homem += 1
    if sexo == 'F' and idade < 20:
        contador_mulher += 1
        
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if opcao == 'N':
        break
          
print (f'Temos {contador_idade} pessoas com mais de 18 anos.')
print (f'Ao todo temos {contador_homem} homens cadastrados.')
print (f'E temos {contador_mulher} mulher(es) com menos de 20 anos.\n')