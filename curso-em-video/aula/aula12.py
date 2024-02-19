nome = str(input('Qual o seu nome? '))

if nome == 'Bruno':
    print ('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paula'or nome == 'Maria' or  nome == 'Gustavo':
    print ('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Déborah':
    print ('Belo nome feminino.')
else:
    print ('Seu nome é  bem normal.')
print (f'Tenha um bom dia {nome}')