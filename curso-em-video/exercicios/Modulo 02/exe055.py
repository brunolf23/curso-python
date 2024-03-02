# Maior e menor da sequência

lista = []
for i in range (1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    lista.append(peso)
maior = max(lista)
menor = min(lista)

print (f'O maior peso é {maior}kg.')
print (f'O menor peso é {menor}kg.')