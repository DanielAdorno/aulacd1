# perguntar o numero de sala disponiveis 

n_salas= int(input('digite o número de salas disponivis '))

#inicializa a lis de lugares vagos com base na entrada de usuario

lugares_vagos = [] 
for i in range (n_salas):
    lugares= int (input(f"DIGITE A QUANTIDADE DE LUGARES PARA A SALA {i+1}:"))
    lugares_vagos.append (lugares)
#lista para contar quantos ingresso foram vendidos em cada sala (conforme ex :6.14)

ingressos_vendidos = [0] *len (lugares_vagos) # len (verifica e inclui)

while True:
    sala = int(input("\nSala (0 sai): "))

    if sala == 0:
        break

# condiçoes 

if sala>len (lugares_vagos) or sala <1 :
    print ('Sala inválida')
elif lugares_vagos [sala -1]==0:
    print ('desculpe ,  sala lotada !')
else: 
    luga_desejados = int(input(f'Quantos lugares vc deseja ({lugares_vagos[sala - 1]}vagos):'))
    
    if lugares_desejados > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
    elif lugares_desejados < 0:
            print("Número inválido")
    else:
            lugares_vagos[sala - 1] -= lugares_desejados
            ingressos_vendidos[sala - 1] += lugares_desejados
            print(f"{lugares_desejados} lugares vendidos")

print("\nUtilização das salas")
total_geral_vendas = 0
for i, l in enumerate(lugares_vagos):
    print(f"Sala {i + 1} – {l} lugar(es) vazio(s) - {ingressos_vendidos[i]} ingresso(s) vendido(s)")
    total_geral_vendas += ingressos_vendidos[i]

print(f"\nTotal de ingressos vendidos no fim do programa: {total_geral_vendas}")
