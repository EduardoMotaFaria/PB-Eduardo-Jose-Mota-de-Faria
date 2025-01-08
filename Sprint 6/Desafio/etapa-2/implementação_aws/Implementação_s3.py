import boto3
from datetime import datetime

access_key = input("Digite a Acess Key: ")
secret_access_key = input("Digite a Secret Acess Key: ")
session_token = input("Digite o Session Token: ")

s3 = boto3.resource(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token
)

nome_bucket = "bucket-desafio-final"

try:
    s3.create_bucket(Bucket=nome_bucket)
    print(f"Bucket '{nome_bucket}' Criado com Sucesso")
except Exception as e:
    print(f"Erro ao criar '{nome_bucket}': {e}")

data_atual = datetime.now()
ano, mes, dia = data_atual.year, f"{
    data_atual.month:02}", f"{data_atual.day:02}"
caminho_s3_filmes = f"Raw/Local/CSV/Movies/{ano}/{mes}/{dia}/movies.csv"
caminho_s3_series = f"Raw/Local/CSV/Series/{ano}/{mes}/{dia}/series.csv"

caminho_do_csv_filmes = "/app/movies.csv"
caminho_do_csv_series = "/app/series.csv"

try:
    s3.meta.client.upload_file(
        caminho_do_csv_filmes, nome_bucket, caminho_s3_filmes)
    print(f"Subindo CSV movies para o '{caminho_s3_filmes}'")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")

try:
    s3.meta.client.upload_file(
        caminho_do_csv_series, nome_bucket, caminho_s3_series)
    print(f"Subindo CSV series para o '{caminho_s3_series}'")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")
