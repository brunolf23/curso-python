pre = float(input('Digite o preço do produto: R$'))
por = int(input('Qual o desconto?: '))
des = pre - (pre * por/100)

print(f'O valor final com o desconto de {por}% é: R${des:.2f}')