# Simulador de Caixa Eletrônico

print('=' * 35 + f'\n{'  CAIXA ELETRÔNICO  ':-^35}\n' + '=' * 35)
valorSaque = int(input('VALOR SAQUE: R$ '))
print('-' * 35)

cedula50, cedula20, cedula10, cedula1 = 0, 0, 0, 0

while True:
    if valorSaque == 0:
        break

    if valorSaque >= 50:
        valorSaque -= 50
        cedula50 += 1
    elif valorSaque >= 20:
        valorSaque -= 20
        cedula20 += 1
    elif valorSaque >= 10:
        valorSaque -= 10
        cedula10 += 1
    elif valorSaque >= 1:
        valorSaque -= 1
        cedula1 += 1

print(f'{'  SAQUE  ': ^35}\n' + '-' * 35)
if cedula50 != 0:
    print(f'{cedula50:10} CÉDULAS DE R${'50':2}')
if cedula20 != 0:
    print(f'{cedula20:10} CÉDULAS DE R${'20':2}')
if cedula10 != 0:
    print(f'{cedula10:10} CÉDULAS DE R${'10':2}')
if cedula1 != 0:
    print(f'{cedula1:10} CÉDULAS DE R${'1':>2}')

print('-' * 35 + f'\n{'SAQUE FINALIZADO': ^35}\n' + '-' * 35)