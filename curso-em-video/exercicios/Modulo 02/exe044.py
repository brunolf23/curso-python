# Gerenciador de Pagamentos

compras = float(input('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO
       [1] À vista dinheiro/pix:
       [2] À vista cartão crédito:
       [3] 2x no cartão:
       [4] 3x ou mais no cartão:''')

opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
    compra1 = compras - (compras * 10/100)
    print (f'Sua compra de R${compras:.2f} vai custar R${compra1:.2f}')
    
elif opcao == 2:
    compra2 = compras - (compras * 5/100)
    print (f'Sua compra de R${compras:.2f} vai custar R${compra2:.2f}')

elif opcao == 3:
    compra3 = compras / 2
    print (f'Sua compra de R${compras:.2f} vai custar 2x R${compra3:.2f}')
    
elif opcao == 4:
    compra4 = compras + (compras * 20/100)
    numero_parcelas = int(input('Quantas parcelas? '))
    parcela = compra4 / numero_parcelas 
    print (f'Sua compra de R${compras:.2f} vai custar R${compra4:.2f}')
    print (f'Parcelado em x{numero_parcelas} de R${parcela}')
    
else:
    print ('OPÇÃO INVÁLIDA')