# Manipulando Texto

frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.'
print (frase.replace('sed', 'Bruno Lindo'))
print (len(frase))
print (frase.count('o'))
print (frase.lower().find('ipsum'))
print (frase.split())
print (frase.capitalize())
print (frase.title())
print ('-'.join(frase))

dividido = frase.split()
print (dividido[2] [2])