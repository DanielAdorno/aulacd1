lugares_vagos=[10,2,1,3,4]#lista para contar quantos ingressos foram vendidos em cada sala 
ingressos_vendidos = [0]*len(lugares_vagos)

while True:   #luoop infinito (como a condição é sempre verdadeira o codigo dentro dele roda repetidamente ate que seja forçado a parar)
    sala= int(input('sala(0 sai)'))
    if sala == 0:
        break #(interronper e sair imediatamente de um loop )
    
    if not (1<= sala <= len (lugares_vagos)):    # if estrutura fundamental usada para tomada de decisão
        print ('sala inválida')
    
    elif lugares_vagos[1] == 0:  #acesse uma posiçao dentro da lista 
        print('Desculpe ,  sala lotada ')
    
    else:
        lugares=int(input (f"Quantos lugares você deseja({lugares_vagos [sala-1]}vagos):"))
    
    if lugares> lugares_vagos [sala-1]:
        print('Esse número de lugares não esta disponível  ')
    
    elif lugares <0 :
        print ('Número inválido')

    else: 
        lugares_vagos [sala -1 ]-= lugares # increment o contados de  ingressos vendidos 
        ingressos_vendidos [sala -1] += lugares 
        print (f"{lugares }lugares vendidos ")
print("\nUtilização das salas")
total_geral_vendas = 0
for i, l in enumerate(lugares_vagos):
    print(f"Sala {i + 1} – {l} lugar(es) vazio(s) - {ingressos_vendidos[i]} ingresso(s) vendido(s)")
    total_geral_vendas += ingressos_vendidos[i]

print(f"\nTotal de ingressos vendidos no fim do programa: {total_geral_vendas}")
