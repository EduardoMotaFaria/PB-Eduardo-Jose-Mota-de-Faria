import json

caminho_arquivo = 'person.json'

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
