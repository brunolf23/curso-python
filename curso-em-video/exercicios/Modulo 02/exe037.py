# Conversor de Bases Numéricas

numero = int(input('Digite um numero inteiro: '))
print ('Qual será a base de conversão?\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal')

opcao = int(input('Digite: '))

numero_binario = bin(numero)
numero_octal = oct(numero)
numero_hexadecimal = hex(numero)

if opcao == 1:
    print (f'O número {numero} convertido para Binário: {numero_binario[2:]}')
    
elif opcao == 2:
    print (f'O número {numero} convertido para Octal: {numero_octal[2:]}')
    
elif opcao == 3:
    print (f'O número {numero} convertido para Hexadecimal: {numero_hexadecimal[2:]}')
    
else:
    print ('Comando inválido!')