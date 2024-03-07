# Aprovando Empréstimo

valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário? R$'))
ano = int(input('Em quantos anos de financiamento? '))

valor_mensal = valor / (ano * 12)
minimo = salario * 30/100

print (f'Para pegar uma casa no valor de R${valor} em {ano} anos, a prestação sera de R${valor_mensal:.2f}.')

if valor_mensal >= minimo:
    print ('Empréstimo NEGADO!')
    
else:
    print ('Empréstimo APROVADO!')