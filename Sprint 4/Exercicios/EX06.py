def maiores_que_media(conteudo: dict) -> list:
    media_preco = sum(conteudo.values()) / len(conteudo)

    produtos_filtrados = filter(
        lambda item: item[1] > media_preco, conteudo.items())

    produtos_ordenados = sorted(produtos_filtrados, key=lambda item: item[1])

    return produtos_ordenados
