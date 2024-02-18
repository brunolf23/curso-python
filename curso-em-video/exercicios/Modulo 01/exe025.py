# Procurando uma string dentro de outra

nome = str(input('Qual o seu nome completo? ')).strip()

print (f'Seu nome tem Silva? {'silva' in nome.lower()}')