# Estatísticas em produtos

total_gasto = produto_caro = menor = contador = 0
barato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    contador += 1
    opcao = ' '
    total_gasto += preco
    
    if preco > 1000:
        produto_caro += 1
    
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome

    while opcao not in 'SN':
        opcao = str(input('Continuar comprando? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('FIM DO PROGRAMA')
print(f'O total da compra foi R$: {total_gasto}')
print(f'O produto mais barato foi {barato} que custa R$: {menor:.2f}')