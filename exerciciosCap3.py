# nota = 6
# media = 7
# aprovado = nota > media
# print(aprovado)

# salario_recebido = 2000
# paga_imposto = salario_recebido > 1200
# print(paga_imposto)

# materia1 = 8
# materia2 = 8
# materia3 = 8
# aprovado = materia1 >= 7 and materia2 >= 7 and materia3 >= 7
# print(aprovado)

# A = 1
# B = 2
# C = True
# D = False
# print (A > B  and C or D)

# A = 10
# B = 3
# C = False
# D = False
# print (A > B  and C or D)

# A = 5
# B = 1
# C = True
# D = True
# print (A > B  and C or D)

#3 * 0.1
#print(3 * 0.1)

#Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não
#pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
# salario2 = 1300
# paga_imposto = salario2 > 1200
# print(paga_imposto)

#Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi
#ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
#que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
#está armazenada nas seguintes variáveis: Matérial, Matéria2 e Matéria3. 
# materia1 = float(input("Digite sua nota"))
# materia2 = float(input("Digite sua nota"))
# materia3 = float(input("Digite sua nota"))
# aprovado = materia1 > 7 and materia2 > 7 and materia3 > 7
# print("Aprovado:", aprovado)

#Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela
# n1 = int(input("Digite um número"))
# n2 = int(input('Digite outro número'))
# print("a soma de N1 + N2 é", n1 + n2)

#Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros. 
# tamanho = float(input('Digite o tamanho em metros'))
# print("O tamanho é de", tamanho*1000, "milímetros")

#Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
# dia = int(input(' Digite a quantidade de dias'))
# horas = int(input(' Digite a quantidade de horas'))
# minutos = int(input(' Digite a quantidade de minutos'))
# segundos = int(input(' Digite a quantidade de segundos'))
# total = (dia * 86400) + (horas * 3600) + (minutos * 60) + segundos
# print('O total de segundos é:', total)

#Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = int(input('Digite seu salário'))
percentual = float(input('Digite o percentual de aumento do seu salário'))
valorAumento = salario * (percentual / 100 )
print('Meu salário tera aumento de', valorAumento )
print('Meu novo salário é', salario + valorAumento ,)

#Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input('Digite o preço da mercadoria'))
desconto = float(input('Digite o percentual de desconto'))
valorDesconto = preco * (desconto / 100)
print('O Desconto será de', valorDesconto)
precoFinal = preco - valorDesconto
print('Vou pagar o total de', precoFinal, 'na mercadoria')

#Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Digite quantos quilômetros você vai percorrer na viajem'))
velocidade = int(input('Digite a velocidade média que você vai manter na viajem'))
tempo = distancia / velocidade
print('O tempo total da viajem será', tempo, 'horas')

# exercicio 3.13 Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: F = 9 × C / 5 + 32
c = float(input('Digite a temperatura em Cº'))
f = (9 * c) / 5 + 32
print('A temperatura em fahrenheit é', f,'Fº' )

#Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
distancia = int(input('Digite a quantidade de km percorrido'))
tempo = int(input('Digite quantos dias ficou com carro alugado'))
valorTotal = (tempo * 60) + (distancia * 0.15)
print('O valor total do aluguel é de R$', valorTotal, )

# Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
quantidade = int(input('Quantos cigarros você fuma por dia?'))
tempo = int(input('Há quantos anos você fuma?'))
totalDia = tempo * 365
print(totalDia, 'dias')
totalCigarros = quantidade * totalDia
print('Você já fumou um total de', totalCigarros, 'cigarros')
tempoMenosVida = totalCigarros * 10
print('A cada cigarro você perde 10 minutos, você já perdeu', tempoMenosVida, 'minutos de vida que equivale a', tempoMenosVida / 1440, 'dias')