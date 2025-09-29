# Atividade 3 

print("\n\n=== Desafio 3 ===")
soma = 0
for i in range(1, 51):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print("Soma =", soma)