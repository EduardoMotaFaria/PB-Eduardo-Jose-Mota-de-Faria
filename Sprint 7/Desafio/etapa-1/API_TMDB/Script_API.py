import json
import boto3
import tmdbv3api
from datetime import datetime

tmdb = tmdbv3api.TMDb()
tmdb.api_key = 'Sua_Chave_API'
movie_api = tmdbv3api.Movie()
company_api = tmdbv3api.Company()

s3_client = boto3.client('s3')
nome_bucket = 'Seu_Bucket'

SCI_FI_GENRE_ID = 878
FANTASY_GENRE_ID = 14
PARAMOUNT_COMPANY_ID = 4


def serialize_asobj(obj):
    if hasattr(obj, "_dict_"):
        return {key: value for key, value in vars(obj).items() if isinstance(value, (str, int, float, bool, list, dict))}
    return {}


def fetch_details_and_credits(movie_id):
    details = movie_api.details(movie_id)
    credits = movie_api.credits(movie_id)

    cast_list = list(credits.cast)[:10]

    return {
        "id": details.id,
        "titulo": details.title,
        "descricao": details.overview,
        "release_date": details.release_date,
        "generos": [{"name": genre.name} for genre in details.genres],
        "generos_ids": [genre.id for genre in details.genres],
        "companhias_producao": [{"id": company.id, "name": company.name} for company in details.production_companies],
        "elenco": [member.name for member in cast_list],
        "direcao": [{"name": member.name, "job": member.job} for member in credits.crew if member.job in ["Director", "Writer"]]
    }


def fetch_filtered_movies(max_results=100):
    results = []
    page = 1
    max_pages = 17

    while len(results) < max_results:
        response = movie_api.popular(page=page)

        if not response:
            break

        for movie in response:
            movie_details = fetch_details_and_credits(movie.id)

            genre_ids = set(movie_details.get("genre_ids", []))
            production_companies = movie_details.get(
                "production_companies", [])

            if (
                {SCI_FI_GENRE_ID, FANTASY_GENRE_ID} & genre_ids and
                any(company["id"] ==
                    PARAMOUNT_COMPANY_ID for company in production_companies)
            ):
                results.append(movie_details)

            if len(results) >= max_results:
                break

        page += 1
        if page > max_pages:
            break

    return results[:max_results]


def save_to_s3(data, file_name):
    timestamp = datetime.now().strftime('%Y/%m/%d')
    s3_file_path = f"TMDB/Movies/{timestamp}/{file_name}"

    json_data = json.dumps(data, ensure_ascii=False,
                           indent=4, default=lambda o: serialize_asobj(o))

    s3_client.put_object(
        Bucket=nome_bucket,
        Key=s3_file_path,
        Body=json_data,
        ContentType='application/json'
    )

    print(f"Arquivo enviado para o S3: {s3_file_path}")


def lambda_handler(event, context):
    filtered_movies = fetch_filtered_movies(max_results=100)

    save_to_s3(filtered_movies, f"filmes_{
               datetime.now().strftime('%Y%m%d%H%M%S')}.json")

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Filmes enviados com sucesso para o S3!'})
    }
