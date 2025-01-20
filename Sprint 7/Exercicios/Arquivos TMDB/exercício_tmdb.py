import requests
import pandas as pd
from IPython.display import display

chave_api = input('Chave da API: ')

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={
    chave_api}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df = {'Titulo': movie['title'],
          'Data de lançamento': movie['release_date'],
          'Visão Geral': movie['overview'],
          'Votos': movie['vote_count'],
          'Média de Votos': movie['vote_average']}
    filmes.append(df)


df = pd.DataFrame(filmes)
display(df)
