import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, trim, when, monotonically_increasing_id, to_date
from awsglue.context import GlueContext
from awsglue.transforms import Relationalize
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

spark = SparkSession.builder.appName("TratamentoFilmes").getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

input_path = args['S3_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

dyf = glueContext.create_dynamic_frame.from_options(
    format_options={"useGlueParquetWriter": True},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [input_path], "recurse": True}
)

df = dyf.toDF()

df = df.withColumn("genre", explode(col("genres"))) \
       .withColumn("id_genre", col("genre.id")) \
       .withColumn("name_genre", col("genre.name")) \
       .drop("genre", "genres")

df = df.withColumn("company", explode(col("production_companies"))) \
       .withColumn("id_company", col("company.id")) \
       .withColumn("name_company", col("company.name")) \
       .drop("company", "production_companies")

df = df.withColumn("total_revenue", col("revenue.int")).drop("revenue")

df = df.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd"))

directors_df = df.select("director").distinct().withColumn(
    "id_director", monotonically_increasing_id())


df = df.join(directors_df, on="director", how="left")

df = df.withColumn("imdb_id", trim(col("imdb_id"))) \
       .withColumn("original_title", trim(col("original_title"))) \
       .withColumn("director", trim(col("director"))) \
       .withColumn("name_company", trim(col("name_company"))) \
       .withColumn("name_genre", trim(col("name_genre"))) \
       .withColumn("popularity", when(col("popularity").isNull(), 0).otherwise(col("popularity"))) \
       .withColumn("vote_average", when(col("vote_average").isNull(), 0).otherwise(col("vote_average"))) \
       .withColumn("vote_count", when(col("vote_count").isNull(), 0).otherwise(col("vote_count")))\
       .withColumn("budget", when(col("budget").isNull(), 0).otherwise(col("budget")))


df_generos = df.select("id_genre", "name_genre").dropDuplicates()
df_diretores = df.select("id_director", "director").dropDuplicates()
df_companhias = df.select("id_company", "name_company").dropDuplicates()
df_filmes = df.select("imdb_id", "original_title", "release_date")
df_fato_filmes = df.select("imdb_id", "id_genre", "id_director", "id_company",
                           "popularity", "vote_average", "vote_count", "total_revenue", "budget")


df_generos.coalesce(1).write.mode(
    "overwrite").parquet(f"{output_path}/dim_generos")
df_diretores.coalesce(1).write.mode(
    "overwrite").parquet(f"{output_path}/dim_diretores")
df_companhias.coalesce(1).write.mode(
    "overwrite").parquet(f"{output_path}/dim_companhias")
df_filmes.coalesce(1).write.mode(
    "overwrite").parquet(f"{output_path}/dim_filmes")
df_fato_filmes.coalesce(1).write.mode(
    "overwrite").parquet(f"{output_path}/fato_filmes")

job.commit()
