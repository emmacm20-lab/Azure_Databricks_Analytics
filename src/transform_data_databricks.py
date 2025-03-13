# 📂 src/transform_data_databricks.py - Transformaciones con Spark en Databricks

from pyspark.sql import SparkSession

def transform_data():
    spark = SparkSession.builder.appName("Data Transformation").getOrCreate()
    df = spark.read.parquet("dbfs:/mnt/data/datos.parquet")
    df_transformed = df.withColumnRenamed("old_column", "new_column")
    df_transformed.write.mode("overwrite").parquet("dbfs:/mnt/data/datos_limpiados.parquet")
    print("Transformación completada.")

if __name__ == "__main__":
    transform_data()