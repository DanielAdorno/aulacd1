# atividade 
# pergunte 4 notas e mostre e mostre a media delas 
""""
A+ = 9.5 a 10
A = 9.0 a 9.4
B+ = 8.5 a 8.9
B = 8.0 a 8.4
C+ = 7.5 a 7.9
C = 7.0 a 7.4
D = 6.0 a 6.9
F > 6.0
"""
notas = []
while len(notas) < 4:
    try:
        nota = float(input(f"Digite a nota {len(notas)+1}: "))
        notas.append(nota)
    except ValueError:
        print("Por favor, digite um número válido.")

soma = sum(notas)
media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")


if media >= 9.5:
    print("A+")
elif media >= 9.0:
    print("A")
elif media >= 8.5:
    print("B+")
elif media >= 8.0:
    print("B")
elif media >= 7.5:
    print("C+")
elif media >= 7.0:
    print("C")
elif media >= 6.0:
    print("D")
else:    
    print("F")