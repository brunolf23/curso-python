# Estatísticas em produtos

total_gasto = produto_caro = 0

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    opcao = ' '
    total_gasto += preco
    
    if preco > 1000:
        produto_caro += 1
    
    # adicionar o nome do produto mais barato

    while opcao not in 'SN':
        opcao = str(input('Continuar comprando? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print (f'Finalizado {produto_caro}\n')