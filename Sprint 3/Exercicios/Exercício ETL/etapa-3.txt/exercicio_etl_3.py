with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    dados = arquivo.readlines()


def encontrar_ator_maior_media_receita(dados):
    maior_media_receita = 0
    ator_maior_media_receita = ""

    for linha in dados[1:]:
        colunas = linha.strip().split(",")

        if len(colunas) > 6:
            colunas[0] = f"{colunas[0]},{colunas[1]}"
            colunas.pop(1)

        ator = colunas[0].strip('"')
        media_receita = float(colunas[3].strip())

        if media_receita > maior_media_receita:
            maior_media_receita = media_receita
            ator_maior_media_receita = ator

    return ator_maior_media_receita, maior_media_receita


ator_maior_media, media_receita = encontrar_ator_maior_media_receita(dados)

print(f"O ator/atriz com a maior média de receita por filme é {
      ator_maior_media}, com média de ${media_receita:.2f} milhões.")
