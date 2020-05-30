print('Olá usuário! Seja bem vindo!')
nome = str(input('Por favor, informe seu nome: '))
idade = int(input('Sua idade: '))
sexo = str(input('Seu sexo: '))
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kilos: '))
calc = altura * peso /5

print('{}, com {} anos, sendo do sexo {}, seu imc é de {}' .format(nome, idade, sexo, calc))
