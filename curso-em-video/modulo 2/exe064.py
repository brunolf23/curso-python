# Tratando vários valores v.1.0

num = contNum = acumulador = 0
while num != 999:
    contNum += 1
    acumulador += num
    num = int(input('Informe um valor ou 999 para sair: '))
print(f'\nForam informados {contNum - 1} números\nE a soma entre eles é {acumulador}')