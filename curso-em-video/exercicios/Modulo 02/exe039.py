#Alistamento Militar

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print (f'Quem nasceu em {ano} tem {idade} anos, você ainda vai se alistar ao serviço militar. \nFalta(m) {saldo} ano(s).')
    ano_futuro = atual + saldo
    print (f'Seu alistamento será em {ano_futuro}.')
    
elif idade == 18:
    print (f'Quem nasceu em {ano} tem {idade} ano(s), está na hora do alistamento militar.')
    
elif idade > 18:
    saldo = idade - 18
    print (f'Você tem {idade} ano(s), já passou do tempo do alistamento militar. \nPassou {saldo} ano(s).')
    ano_passado = atual - saldo
    print (f'Seu alistamento foi em {ano_passado}.')