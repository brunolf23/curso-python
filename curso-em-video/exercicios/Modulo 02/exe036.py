valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você ira pagar? '))

valor_mensal = valor / (ano * 12)

if valor_mensal > (salario + 30/100):
    print ('O empréstimo está negado!')
else:
    print ('Você ira conseguir o empréstimo')