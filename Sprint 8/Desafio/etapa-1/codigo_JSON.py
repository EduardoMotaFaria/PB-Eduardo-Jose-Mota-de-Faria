import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_JSON_PATH', 'S3_TARGET_PARQUET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

target_path_parquet = f"{args['S3_TARGET_PARQUET_PATH']}"


datasource_json = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_JSON_PATH']]},
    format="json"
)

df_json = datasource_json.toDF()
df_json.coalesce(1).write.parquet(target_path_parquet, mode='overwrite')

job.commit()
