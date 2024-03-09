# Maior e Menor valores

resposta = 'SIM'
acumulador = contador = calculo = maior = menor = 0

while resposta in 'SIM':
    num = int(input('Digite um número inteiro: '))
    acumulador += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    resposta = str(input('Deseja continuar? [Sim/Não] ')).upper()
calculo = acumulador / contador
print (f'Você digitou {contador} números e a média foi {calculo}')
print (f'O maior valor é {maior} e o menor {menor}.')