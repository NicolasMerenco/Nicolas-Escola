# Atividade 5


print("\n=== Desafio 5 ===")
soma = 0
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        soma += num
print("Soma dos pares:", soma)