"""#Validador de parenteses

expressao = input("Digite a expressão: ")
pilha = []
x = 0 
while x < len(expressao):
    if expressao[x] == "(":
        pilha.append("(")
    if expressao[x] == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            print("Expressão inválida")
            break
    x += 1

 if len(pilha) == 0:
    print("Expressão válida")
else:   
    print("Expressão inválida")"""

l=[2,4,6,8,10]
for c in l:
    print(c)