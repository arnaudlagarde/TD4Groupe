from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, DoubleType, TimestampType

# Initialiser la session Spark
spark = SparkSession.builder \
    .appName("KafkaToHDFS") \
    .getOrCreate()

# Définir le schéma des données pour topic1
schema_topic1 = StructType([
    StructField("date", TimestampType(), True),  # Format heure-date
    StructField("secousse", BooleanType(), True),
    StructField("magnitude", DoubleType(), True),
    StructField("tension_entre_plaque", DoubleType(), True)
])

# Définir le schéma des données pour topic2
schema_topic2 = StructType([
    StructField("date", TimestampType(), True),  # Format heure-date
    StructField("ville", StringType(), True),
    StructField("secousse", BooleanType(), True),
    StructField("magnitude", DoubleType(), True),
    StructField("tension_entre_plaque", DoubleType(), True)
])

# Lire les données de Kafka pour les deux topics
kafka_df1 = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "topic1") \
    .option("startingOffsets", "latest") \
    .load()

kafka_df2 = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "topic2") \
    .option("startingOffsets", "latest") \
    .load()

# Convertir la colonne Kafka 'value' de string à format structuré pour topic1
structured_df1 = kafka_df1.select(
    from_json(col("value").cast("string"), schema_topic1).alias("data")
).select("data.*")

# Convertir la colonne Kafka 'value' de string à format structuré pour topic2
structured_df2 = kafka_df2.select(
    from_json(col("value").cast("string"), schema_topic2).alias("data")
).select("data.*")

# Écrire les données de topic1 dans HDFS
query1 = structured_df1.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hdfs://namenode:9000/data/seismic") \
    .option("checkpointLocation", "hdfs://namenode:9000/checkpoints/topic1") \
    .option("startingOffsets", "earliest") \
    .start()

# Écrire les données de topic2 dans HDFS
query2 = structured_df2.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hdfs://namenode:9000/data/cities") \
    .option("checkpointLocation", "hdfs://namenode:9000/checkpoints/topic2") \
    .option("startingOffsets", "earliest") \
    .start()

# Attendre la fin des requêtes
query1.awaitTermination()
query2.awaitTermination()
