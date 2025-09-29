# Atividade 7

print("\n\n=== Desafio 7 ===")
frase = input("Digite uma frase: ").replace(" ", "").lower()
if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")