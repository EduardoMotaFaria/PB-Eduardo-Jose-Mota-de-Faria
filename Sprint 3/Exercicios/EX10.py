def remover_elementos(lista):
    return list(set(lista))


lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

resultado = remover_elementos(lista)
print(resultado)
