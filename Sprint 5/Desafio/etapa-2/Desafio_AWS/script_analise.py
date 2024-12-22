import pandas as pd

caminho_dataset = 'Contratos_Capes_Tratado.csv'

dataset = pd.read_csv(caminho_dataset, encoding='utf-8',
                      delimiter=';')

# "Qual é o valor total e a média dos contratos no tipo 'Serviços', assinados entre 2020 e 2023, com a moeda 'BRL'? é possível adicionar uma coluna indicando o valor do contrato excede 500.000 BRL e converter esses valores para ter o resultado com 2 casas depois da virgula?"


dataframe = pd.DataFrame(data=dataset)

filtrando_dados = dataframe[(dataframe['TP_CONTRATO'] == 'Servicos') &
                            (dataframe['CD_MOEDA'] == 'BRL') &
                            (dataframe['AN_INICIO_VIGENCIA'] >= '2020-01-01') &
                            (dataframe['AN_INICIO_VIGENCIA'] <= '2023-12-31')]

filtrando_dados = filtrando_dados[filtrando_dados['TP_CONTRATO'].str.contains(
    'Servicos', case=False, na=False)]

valor_total = filtrando_dados['VL_CONTRATO'].sum()
valor_media = filtrando_dados['VL_CONTRATO'].mean()

filtrando_dados['CONTRATO_ACIMA_500K'] = filtrando_dados['VL_CONTRATO'].apply(
    lambda x: 'Sim' if x > 500000 else 'Não')

filtrando_dados['VL_CONTRATO'] = filtrando_dados['VL_CONTRATO'].astype(float)

filtrando_dados.to_csv('resultado_filtrado.csv', index=False)

print(f"Valor total de contratos:{valor_total}")
print(f"media dos valores do contrato:{valor_media:.2f}")
print(filtrando_dados)
