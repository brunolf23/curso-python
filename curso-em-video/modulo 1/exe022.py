# Analisador de Textos

nome = str(input('Digite seu nome completo: ')).strip()
print ('Analisando seu nome...')
print (f'Seu nome em maiúsculas é {nome.upper()}.')
print (f'Seu nome em minúsculas é {nome.lower()}.')
print (f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
print (f'O seu primeiro nome tem {nome.find(' ')} letras.')

contando = nome.split()
print (f'O seu primeiro nome tem {len(contando[0])} letras.')