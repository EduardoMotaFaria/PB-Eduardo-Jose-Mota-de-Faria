with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    dados = arquivo.readlines()


def contar_aparicoes_filmes(dados):
    filmes_contagem = {}

    for linha in dados[1:]:
        colunas = linha.strip().split(",")

        if len(colunas) > 6:
            colunas[0] = f"{colunas[0]},{colunas[1]}"
            colunas.pop(1)

        filme_mais_bilheteira = colunas[4].strip('"')

        if filme_mais_bilheteira in filmes_contagem:
            filmes_contagem[filme_mais_bilheteira] += 1
        else:
            filmes_contagem[filme_mais_bilheteira] = 1

    filmes_ordenados = sorted(filmes_contagem.items(),
                              key=lambda x: (-x[1], x[0]))

    return filmes_ordenados


filmes_mais_bilheteiros = contar_aparicoes_filmes(dados)

print("Contagem de aparições dos filmes de maior bilheteira:")
for filme, contagem in filmes_mais_bilheteiros:
    print(f"{filme}: {contagem} aparições")
