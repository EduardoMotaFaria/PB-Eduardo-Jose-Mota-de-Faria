caminho_arquivo = 'arquivo_texto.txt'

with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo, end='')
