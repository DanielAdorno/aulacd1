# numero = 1

# while numero <=5:
#     print(numero)
#     numero = numero + 1

# contador = 5

# while contador > 0:
#     print(contador)
#     contador = contador - 1

# numero = 1

# while numero <=10:
#     print(numero)
#     numero = numero + 1

# #Exercício 5.1 Modifique o programa para exibir os números de 1 a 100.
# numero = 1
# while numero <=100:
#     print(numero)
#     numero = numero + 1

#Exercício 5.2 Modifique o programa para exibir os números de 50 a 100.

# numero = 50

# while numero <= 100:
#     print(numero)
#     numero = numero + 1

# contagem = 10

# while contagem >= 0:
#     print(contagem)
#     contagem = contagem - 1

# print("Fogo!")

# #Contadores
# fim = int(input("Digite o último número a imprimir: "))
# x = 1

# while x <= fim:
#     print(x)
#     x = x + 1

# #Agora refaça o programa anterior para imprimir apenas os números pares entre 0 e um número digitado pelo usuário.
# fim = int(input("Digite o último número: "))
# x = 0

# while x <= fim:
#     print(x)
#     x = x + 2

# #Outra Maneira
# fim = int(input("Digite o último número: "))
# x = 0

# while x <= fim:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

#Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

# fim = int(input("Digite o último número: "))
# x = 1

# while x <= fim:
#     print(x)
#     x = x + 2

#Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
# x = 1

# while x <= 10:
#     print(x * 3)
#     x = x + 1

#Vejamos outro tipo de problema. Imagine ter de imprimir a tabuada de adição de um número digitado pelo usuário. Essa tabuada deve ser impressa de 1 a 10, sendo no número digitado pelo usuário. Teríamos, assim, n+ 1, n+2, ... n+ 10.

# n = int(input("Tabuada de: "))

# x = 1

# while x <= 10:
#     print(n + x)
#     x = x + 1

# n = int(input("tabuada de: "))

# x = 1

# while x <= 10:
#     print(f"{n} + {x} = {n + x}")
#     x = x + 1

#Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2xl = 2, 2x2 = 4, ...
# n = int(input("Tabuada de: "))

# x = 1

# while x <= 10:
#     print(f"{n} x {x} = {n * x}")
#     x = x + 1

# Exercício 5.7 Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10

# n = int(input("Tabuada de: "))
# inicio = int(input("Começar em: "))
# fim = int(input("Terminar em: "))

# x = inicio

# while x <= fim:
#     print(f"{n} x {x} = {n * x}")
#     x = x + 1

#Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))

# resultado = 0
# contador = 1

# while contador <= b:
#     resultado = resultado + a
#     contador = contador + 1

# print("Resultado:", resultado)

#Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenasos operadores de soma e subtração para calcular o resultado. Lembre-se de quepodemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 .;- 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

# dividendo = int(input("Digite o dividendo: "))
# divisor = int(input("Digite o divisor: "))

# quociente = 0
# resto = dividendo

# while resto >= divisor:
#     resto = resto - divisor
#     quociente = quociente + 1

# print("Quociente:", quociente)
# print("Resto:", resto)

#Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito = float(input("Depósito inicial: R$ "))
taxa = float(input("Taxa de juros mensal (%): "))

saldo = deposito
mes = 1

while mes <= 24:
    juros = saldo * (taxa / 100)
    saldo = saldo + juros

    print(f"Mês {mes}: R$ {saldo:.2f}")

    mes = mes + 1

ganho_total = saldo - deposito

print(f"Total ganho com juros em 24 meses: R$ {ganho_total:.2f}")