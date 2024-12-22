import pandas as pd
from unidecode import unidecode

caminho_dados_contratos = 'Contratos_Capes.csv'

dados_contratos = pd.read_csv(caminho_dados_contratos, encoding='utf-8',
                              delimiter=';')


def remover_acentos(texto):
    if isinstance(texto, str):
        return unidecode(texto)
    return texto


def remover_espacos(texto):
    if isinstance(texto, str):
        texto = texto.strip()
        texto = texto.replace('"', '')
        texto = texto.replace("'", '')
    return texto


dados_contratos = dados_contratos.applymap(remover_acentos)
dados_contratos = dados_contratos.applymap(remover_espacos)

dados_contratos['AN_INICIO_VIGENCIA'] = pd.to_datetime(
    dados_contratos['AN_INICIO_VIGENCIA'], format='%d/%m/%Y')

dados_contratos['AN_FIM_VIGENCIA'] = pd.to_datetime(
    dados_contratos['AN_FIM_VIGENCIA'], format='%d/%m/%Y')


dados_contratos.to_csv('Contratos_Capes_Tratado.csv',
                       index=False, encoding='utf-8', sep=';')
