# Atividade 8

print("\n=== Desafio 8 ===")
from datetime import date
ano_atual = date.today().year

maiores = 0
menores = 0

for i in range(7):
    nasc = int(input(f"Ano de nascimento da {i+1}ª pessoa: "))
    idade = ano_atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Maiores de idade: {maiores}")
print(f"Menores de idade: {menores}")