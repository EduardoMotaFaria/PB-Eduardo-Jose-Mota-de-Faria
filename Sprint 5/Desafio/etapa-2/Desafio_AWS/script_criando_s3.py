import boto3

access_key = "ASIA2HVQ5TXCUMSAEYLE"
secret_access_key = "HzQhwnrQxAmIX18O/JsCsuyyy2DhW91b8/giAtxX"
session_token = "IQoJb3JpZ2luX2VjELP//////////wEaCXVzLWVhc3QtMSJHMEUCIQDTc84cQcdpp9i81rd6f/DQfAKbLNma7grG6q3HkM1HwwIgTn0ogJzwRRshdqnwb45PBGM/5yvLOuOuRKLen+Q66qYqnwMIexAAGgw3MDM2NzE5MzQ0MDUiDC9q4oua0E1dnoFhHyr8ArMbyQHllgVtOWWQL9z97QIv9oVXZ0DUQRNq5BH/aql8U3e+8p+SB7rCAmeXvTxe77w2m7jQ591+ICC36rJNOUvor3+hKzbqYTXPlLHXrpQwzD1Lqvn/E+UepcPI6ZgRNEWuSC8phcpwqpq0ee4woWQDuN6QTMuCphc53XPyi1064EHC7wJL6PMpU75/scM33wYzjMyR5WiwEMiRkk399/vD6uFzuBLpO6tZjoqa6MPVC8YVdSdsT/AdOhVZX5JrIZpMbfp2v3h9Kz9zdiE+Qb8Q3UN0HZ6+Fe25e6GAVv1j61ElRn4+9/H1dqfgLptGMQIldo4bPLCpVizYaA5rLvn6ELi+q3uNPiRn0Cvh+lmPwW/XpnYUe1GXsPw0rnEdJcg9hVkEUsPo+lGO5sjJFRIL+Wd6tC0GI2ZNN/bwnK8aPHO8m+CECcKYbh7nPaX+8KiQZXm6z/t95zsYHW/4OUbl6RWUvlhyPuJUcZHyGUAzUVfCTwEMrs+HjNwdMOHAkbsGOqYBaeYCNi/GgwKYhVlotGMK/TWTZzS1FCIJm243OswTaW43wFQlJS6XPKtUfnIPGy5MlmoisT/oh4sU4toYlQ4uDZswX7lcMwM28aRZh+z8KIFKrVX3AKCJTt8aG7D2K0hloJIm7j+NMLLsi85l9tiWE8KuRZvQiCGYjvSRHOJQKgvevQC9qDQckTNjNSpuQjlLxBBHeecwpaWfTbqLnNZSa10c8EvzBw=="

s3 = boto3.resource(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token
)

nome_bucket = "bucket-contratos-capes"

try:
    s3.create_bucket(Bucket=nome_bucket)
    print(f"Bucket '{nome_bucket}' criado com sucesso.")
except Exception as e:
    print(f"Erro ao criar o bucket: {e}")

arquivo_local = "C:/Users/proge/desafio_compass/Desafio_python/Contratos_Capes.csv"

try:
    s3.meta.client.upload_file(
        arquivo_local, nome_bucket, "Contratos_Capes.csv")
    print(f"Arquivo enviado para o bucket '{nome_bucket}'.")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")
