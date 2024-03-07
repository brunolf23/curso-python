# Validação de Dados

sex = str(input('Digite o seu sexo [F/M]: ')).strip().upper()[0]

while sex not in 'FM':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print (f'Sexo {sex} registrado com sucesso.')