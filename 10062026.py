estoque = {
    'alface': [100,10.99],
    'batata': [500,9.99],
    'tomate': [3000,15.99],
    'feijao': [200,12.99],
    'cenoura': [600,15.99],
    }

"""# Entrada venda
venda = []

while obter_venda != '':
    produto, quantidade = obter_venda.split()
    quantidade = int(quantidade)
    venda.append([produto, quantidade])
    obter_venda = input()

# venda = [['tomate',5],['batata', 2], ['cenoura',1],['alface', 10]]
total = 0
print('Vendas:\n')
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco* quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -=quantidade
    total += custo
print(f'Custo total: {total:21.2f}\n')
print('Estoque:\n')
for chave, dados in estoque.items():
    print('Descrição: ',chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados [1]:6.2f}\n')"""

total = 0

print('Vendas:\n')
while True:
    produto = input("Nome do produto (Fim para sair): ")
    if produto == "Fim":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado no estoque.")


print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")