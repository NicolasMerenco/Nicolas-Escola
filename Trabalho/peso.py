# Atividade 9

print("\n=== Desafio 9 ===")
pesos = []
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    pesos.append(peso)

print("Maior peso:", max(pesos))
print("Menor peso:", min(pesos))