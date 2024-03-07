# Soma ímpares múltiplos de três

contador = 0
resto = 0
for soma in range (1, 500, 2):
    if soma % 3 == 0:
        contador = contador + 1
        resto = resto + soma
print (contador, resto)