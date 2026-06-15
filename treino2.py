#pergunte o depósito 
#pergunte a taxa de juros da poupança 
#mostre o saldo mes am durante meses 
#mostre o total ganho com juros no período 

depositoInicial = float(input('Digite o valor do deposito: '))
taxaJuro = float(input('digite a taxa de juro mensal(%): '))
taxaJuro= taxaJuro/100
Saldo = depositoInicial
valorInicial = depositoInicial
for mes in range (1, 25):
    juros= Saldo * taxaJuro 
    Saldo = Saldo + juros

    print (f'Mês {mes}: R$ {Saldo: 2f}')
ganho = Saldo - valorInicial
print (f"\n total ganho com juros: R$ {ganho :2f}")    


