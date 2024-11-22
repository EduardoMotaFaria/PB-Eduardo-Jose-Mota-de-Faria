def dividir_lista(lista):
    tamanho = len(lista)
    parte_tamanho = tamanho // 3

    lista1 = lista[:parte_tamanho]
    lista2 = lista[parte_tamanho:2*parte_tamanho]
    lista3 = lista[2*parte_tamanho:]

    return lista1, lista2, lista3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista(lista)

print(f"{resultado[0]} {resultado[1]} {resultado[2]}")
