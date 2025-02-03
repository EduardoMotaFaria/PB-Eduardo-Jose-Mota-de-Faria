import random
import time
import names

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for _ in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios.")

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

with open("nomes_aleatorios.txt", "w") as file:
    file.write("\n".join(dados))

print("Arquivo nomes_aleatorios.txt gerado com sucesso!")

with open("nomes_aleatorios.txt", "r") as file:
    for _ in range(10):
        print(file.readline().strip())
