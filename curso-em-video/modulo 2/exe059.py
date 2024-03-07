# Criando um Menu de Opções

import time

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    opcao = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
=>  Digite uma opção: '''))
    
    if opcao == 1:
        soma = primeiro + segundo
        print (f'A soma de {primeiro} + {segundo} = {soma}')
        
    elif opcao == 2:
        multi = primeiro * segundo
        print (f'A multiplicação de {primeiro} x {segundo} = {multi}')
        
    elif opcao == 3:
        if primeiro > segundo:
            print (f'Entre o {primeiro} e {segundo} o maior é {primeiro}')
        else:
            print (f'Entre o {primeiro} e {segundo} o maior é {segundo}')
        
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        
    elif opcao == 5:
        print ('Finalizando...')
        time.sleep(3)
        
    else:
        print ('Opção inválida! Tente novamente.')
    print ('--=' *15)
print ('Fim do programa! Volte sempre.')