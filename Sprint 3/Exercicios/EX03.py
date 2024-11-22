numeros = list(range(1, 100))

for numero in numeros:
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                break
        else:
            print(f"{numero}")
