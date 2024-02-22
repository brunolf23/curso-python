# Separando dígitos de um número

numero = int(input('Informe um número: '))

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f'Analisando o número {numero}')
print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')