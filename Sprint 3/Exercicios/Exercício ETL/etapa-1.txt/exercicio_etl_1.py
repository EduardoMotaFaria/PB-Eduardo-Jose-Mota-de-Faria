def arquivo_actors(caminho):
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas


def encontrar_ator_com_mais_filmes(dados):
    maior_filmes = 0
    ator_maior_filmes = ""

    for linha in dados[1:]:
        colunas = linha.strip().split(",")

        if len(colunas) > 6:
            colunas[0] = f"{colunas[0]},{colunas[1]}"
            colunas.pop(1)

        ator = colunas[0].strip('"')
        numero_filmes = int(colunas[2].strip())

        if numero_filmes > maior_filmes:
            maior_filmes = numero_filmes
            ator_maior_filmes = ator

    return ator_maior_filmes, maior_filmes


caminho_arquivo = "actors.csv"

dados = arquivo_actors(caminho_arquivo)

ator, filmes = encontrar_ator_com_mais_filmes(dados)

print(
    f"O ator/atriz com maior número de filmes é {ator} com {filmes} filmes.")
