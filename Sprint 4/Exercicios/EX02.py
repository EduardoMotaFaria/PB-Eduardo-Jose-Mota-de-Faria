def conta_vogais(texto):
    vogais = filter(lambda char: char.lower() in 'aeiou', texto)
    return len(list(vogais))


texto = "Exemplo de texto com algumas vogais"
print(conta_vogais(texto))
