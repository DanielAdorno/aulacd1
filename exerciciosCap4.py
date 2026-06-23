# Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h.
# velocidade = int(input('qual a velocidade você estava dirigindo?'))
# if velocidade > 80:
#     print('você foi Multado!')
#     print('Sua multa é', (velocidade - 80) * 5)

# Programa 4.1 - Lê dois valores e imprime qual é o maior.
# a = int(input( "Primeiro valor: "))
# b = int(input( "Segundo valor: "))
# if a > b:
#     print( "O primeiro valor é o maior!")
# if b > a:
#     print("O segundo valor é o maior!")

# Programa 4.3 - Cálculo do Imposto de Renda
# salario = float(input("Digite seu salário para cálculo do imposto"))
# base = salario
# imposto = 0
# if base> 3000:
#   imposto = imposto + ((base - 3000) * 0.35)
#   base = 3000
# if base> 1000:
#  imposto = imposto + ((base - 1000) * 0.20)
# print(f"Salario: R${salario:6.2f} lmposto a pagar: R${imposto:6.2f}")

#Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.
# n1 = int(input("Digite um número"))
# n2 = int(input("Digite um número"))
# n3 = int(input("Digite um número"))
# if n1 > n2 and n1 > n3:
#     maior = n1
# if n2 > n1 and n2 > n3:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3
# if n1 < n2 and n1 < n3:
#     menor = n1
# if n2 < n1 and n2 < n3:
#     menor = n2
# if n3 < n1 and n3 < n2:
#     menor = n3
# print(maior, menor)

# Exercício4.4 Escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
# 10%. Para os inferiores ou iguais, de 15%.
# salario = float(input('Digite o valor do seu salário'))
# base = 1250
# if salario > base:
#     print('Seu novo salário é', salario + (salario * (10/100)))
# if salario <= base
#     print('Seu novo salário é', salario + (salario * (15/100)))

# Programa 4.4 - Carro novo ou velho, dependendo da idade com else
# idade= int(input(" Digite a idade de seu carro: "))
# if idade <= 3:
#   print( "Seu carro é novo ")
# else:
#   print( "Seu carro é velho")

#Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km
#e R$ 0,45 para viagens mais longas.

# distancia = float(input('Digite quantos Km você vai percorrer'))
# if distancia < 200:
#   print(f'Sua passagem é de R$ {distancia * 0.50:.2f}')
# else:
#   print(f'Sua passagem é de R$ {distancia * 0.45:.2f}')

#Os planos da empresa Tchau são bem interessantes e oferecem preços diferenciados de acordo com a quantidade de minutos usados por mês. Abaixo de 200 minutos, a empresa cobra R 0,20porminuto.Entre200e400minutos,opreçoédeR  0,18. Acima de 400 minutos, o preço por minuto é de R$ 0,15. O Programa 4.5 resolve esse problema:

# minutos = int(input('Digite quantos minutos você utilizou esse mês no telefone.'))
# if minutos < 200:
#     preco = 0.20
# else:
#   if minutos < 400:
#       preco = 0.18
#   else:
#     preco = 0.15

# print(f"Você vai pagar este Mês,R${minutos * preco:.2f}")

# Programa 4.6 - Categoria x preço
# categoria= int(input( "Digite a categoria do produto: "))
# if categoria == 1:
#     preço= 10
# else:
#     if categoria == 2:
#       preço= 18
#     else:
#         if categoria == 3:
#           preço = 23
#         else:
#             if categoria== 4:
#                 preço = 26
#             else:
#                 if categoria== 5:
#                     preço= 31

#                 else:
#                   print( "Categoria inválida, digite um valor entre 1 e 5! ")
#                   preço = 0
# print(f"O preço do produto é: R${preço:.2f}")

#Programa 4.7 - Categoria x preço, usando elif
# categoria = int(input("Digite a categoria do produto :"))
# if categoria == 1:
#     preço= 10
# elif categoria == 2:
#     preço= 18
# elif categoria == 3:
#     preço = 23
# elif categoria == 4:
#     preço= 26
# elif categoria == 5:
#     preço = 31
# else:
#     print(" categoria inválida , digite um valor entre 1 e 5 !")
#     preço = 0
# print(f"O preço do produto é R${preço:.2f}")

# idade = int(input('Digite sua idade'))
# if idade >= 18:
#     print("Pode tirar CNH")
# else:
#     print('Não pode tirar CNH')

# idade = int(input('Digite sua idade'))
# if idade < 12:
#     print('Criança')
# elif idade >= 12 and idade < 17:
#     print('Adolescente')
# else:
#     print('Adulto')

#Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# operacao = input("Digite a operação (+, -, * ou /): ")

# if operacao == "+":
#     resultado = num1 + num2
#     print("Resultado:", resultado)

# elif operacao == "-":
#     resultado = num1 - num2
#     print("Resultado:", resultado)

# elif operacao == "*":
#     resultado = num1 * num2
#     print("Resultado:", resultado)

# elif operacao == "/":
#     if num2 != 0:
#         resultado = num1 / num2
#         print("Resultado:", resultado)
#     else:
#         print("Erro: divisão por zero não é permitida.")

# else:
#     print("Operação inválida!")

# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário: R$ "))
anos = int(input("Digite a quantidade de anos para pagar: "))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")

print(f"Prestação mensal: R$ {prestacao:.2f}")
print(f"Limite permitido (30% do salário): R$ {limite:.2f}")
