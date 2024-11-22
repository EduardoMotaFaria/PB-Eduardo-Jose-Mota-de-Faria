def my_map(lista, f):
    return [f(item) for item in lista]


def potencia_de_2(x):
    return x ** 2


entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(entrada, potencia_de_2)
print(resultado)
