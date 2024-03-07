# Aumentos múltiplos

salario = int(input('Qual o valor do seu salário? R$'))

if salario > 1250:
    aumento = salario + (salario * 10/100)
    print (f'Como você recebe {salario}, tera um adicional de 10%. Indo para R${aumento:.2f}')
    
else:
    aumento = salario + (salario * 15/100)
    print (f'Como você recebe {salario}, tera um adicional de 15%. Indo para R${aumento:.2f}')