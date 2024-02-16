sala = float(input('Qual o valor do salário? R$'))
adicional = int(input('Quantos porcentos esse mês? '))

bonus = sala + (sala * adicional/100)

print(f'Um funcionário(a) que ganhava {sala:.2f}, vai ter um adicional de {adicional}% nesse mês, indo para: R${bonus:.2f}')