import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame


args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH',
                          'S3_TARGET_PATH', 'S3_INPUT_PATH_SERIES', 'S3_TARGET_PATH_SERIES'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

target_path_movies = f"{args['S3_TARGET_PATH']}"
target_path_series = f"{args['S3_TARGET_PATH_SERIES']}"

datasource_movies = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH']]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

df_movies = datasource_movies.toDF()
df_movies.coalesce(1).write.parquet(target_path_movies, mode='overwrite')

datasource_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH_SERIES']]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

df_series = datasource_series.toDF()
df_series.coalesce(1).write.parquet(target_path_series, mode='overwrite')

job.commit()
