# Verificando as primeiras letras de um texto

cidade = str(input('Qual nome da cidade que você nasceu? ')).strip()

print (f'{cidade[:5].upper() == 'SANTO'}')