def arquivo_actors(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()


def calcular_media_receita_bruta(dados):
    soma_receita_bruta = 0
    total_filmes = 0

    for linha in dados[1:]:
        colunas = linha.strip().split(",")

        try:
            receita_bruta = float(colunas[5].strip())
            soma_receita_bruta += receita_bruta
            total_filmes += 1
        except ValueError:
            continue

    media_receita_bruta = soma_receita_bruta / \
        total_filmes if total_filmes > 0 else 0
    return media_receita_bruta


dados = arquivo_actors("actors.csv")

media_receita = calcular_media_receita_bruta(dados)

print(f"A média de receita bruta dos principais filmes é: ${
      media_receita:.2f} milhões.")
