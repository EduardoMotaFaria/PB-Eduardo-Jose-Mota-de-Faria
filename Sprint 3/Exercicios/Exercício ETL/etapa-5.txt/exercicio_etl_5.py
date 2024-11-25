with open('actors.csv', 'r', encoding='utf-8') as arquivo:
    dados = arquivo.readlines()


def calcular_receita_total(dados):
    atores_receita = {}

    for linha in dados[1:]:
        colunas = linha.strip().split(",")

        if len(colunas) > 6:
            colunas[0] = f"{colunas[0]},{colunas[1]}"
            colunas.pop(1)

        ator = colunas[0].strip('"')
        receita_bruta = float(colunas[1].strip())

        if ator in atores_receita:
            atores_receita[ator] += receita_bruta
        else:
            atores_receita[ator] = receita_bruta

    atores_ordenados = sorted(atores_receita.items(), key=lambda x: -x[1])

    return atores_ordenados


atores_receita = calcular_receita_total(dados)

with open('atores_receita_bruta.txt', 'w', encoding='utf-8') as output_file:
    for ator, receita in atores_receita:
        output_file.write(f"{ator} - {receita:.2f}\n")

print("A lista dos atores e suas receitas brutas foi salva em 'atores_receita_bruta.txt'.")
