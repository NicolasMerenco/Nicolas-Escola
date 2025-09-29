# Atividade 1 - Faça um programa que mostre na tela uma contagem regressiva para o estouro,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

print("=== Desafio 1 ===")
for i in range(10, -1, -1): # começa em 10 e vai até 0
    print(i)
    time.sleep(1) # pausa de 1 segundo
print("💥 BOOM! Estouro!")