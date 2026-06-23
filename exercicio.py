#import random
#print(random.randint(1, 10))
#import time

#import time
#print("Olá")
#time.sleep(2)
#print("2 segundos depois")

import random 
import time 
totalNumeros = int (input('Digite a quantidade de números a ser sorteado:'))
inicioSorteio = int(input('Digite o número inicial do sorteio:'))
fimSorteio = int (input('Digite o número final do sorteio:'))
print("-----------")
print (f'Sorteiado os {totalNumeros }números ')
contador=1
SomanumerosSorteados = 0
while contador <= totalNumeros:
    numerosSortiado = random.randint(inicioSorteio,fimSorteio)
    SomanumerosSorteados += numerosSortiado
    print (f'-{numerosSortiado}-')
    time.sleep (0.5)
    contador +=1

print ('-------------')
print (f'Soma dos números sorteados : {SomanumerosSorteados}')
print('--------------')