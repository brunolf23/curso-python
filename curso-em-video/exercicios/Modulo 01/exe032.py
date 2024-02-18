# Ano Bissexto

import datetime

ano = int(input('Qual o ano você gostaria de saber? '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano {ano} é bissexto.')

else:
    print (f'O ano {ano} não é bissexto.')