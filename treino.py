import random 
import time 
totalNumeros = int (input('Digit a quantidade de números: '))
inicio = int (input('Digite o número inicial: '))
fim = int(input('digit o número final: '))
contador = 1
soma = 0
print ('Numeros sortealdos ')
while contador <= totalNumeros:
    numero= random.randint (inicio,fim)
    print (f'-{numero}-')
    soma += numero 
    time.sleep (0.5)
    contador += 1
media = soma/totalNumeros
print("--")
print(f'Soma dos números{soma}')
print ( f'Média dos números :{media}')
print ('----')
