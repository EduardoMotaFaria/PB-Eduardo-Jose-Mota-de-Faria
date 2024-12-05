def processar_numeros(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:

        numeros = map(int, arquivo.readlines())

    numeros_pares = filter(lambda x: x % 2 == 0, numeros)

    numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

    maiores_pares = numeros_pares_ordenados[:5]

    soma_maiores = sum(maiores_pares)

    print(maiores_pares)
    print(soma_maiores)


processar_numeros('number.txt')
