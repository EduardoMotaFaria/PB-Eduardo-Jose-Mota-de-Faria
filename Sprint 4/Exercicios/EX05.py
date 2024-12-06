def ler_notas():
    with open('estudantes.csv', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    def processar_estudantes(linha):
        partes = linha.strip().split(',')
        nome = partes[0]
        notas = list(map(int, partes[1:]))
        tres_maiores = sorted(notas, reverse=True)[:3]
        media_necessaria = round(sum(tres_maiores) / 3, 2)
        return (nome, f"Nome: {nome} Notas: {tres_maiores} Média: {media_necessaria}")

    resultados = sorted(map(processar_estudantes, linhas), key=lambda x: x[0])

    for _, resultado in resultados:
        print(resultado)


ler_notas()
