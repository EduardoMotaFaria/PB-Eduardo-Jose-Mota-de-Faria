import random

random_list = random.sample(range(500), 50)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

sorted_list = sorted(random_list)
n = len(sorted_list)
mediana = sorted_list[n // 2] if n % 2 == 1 else (
    sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {
      valor_minimo}, Máximo: {valor_maximo}")
