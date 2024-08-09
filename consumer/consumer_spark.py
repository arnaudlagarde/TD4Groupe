# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Créer la session Spark
spark = SparkSession.builder \
    .appName("KafkaAsteroidsToHDFS") \
    .getOrCreate()

# Définir le schéma des messages JSON concernant les astéroïdes
asteroid_schema = StructType([
    StructField("id", StringType(), True),
    StructField("position", StructType([
        StructField("x", DoubleType(), True),
        StructField("y", DoubleType(), True),
        StructField("z", DoubleType(), True),
    ]), True),
    StructField("velocity", StructType([
        StructField("vx", DoubleType(), True),
        StructField("vy", DoubleType(), True),
        StructField("vz", DoubleType(), True),
    ]), True),
    StructField("size", DoubleType(), True),
    StructField("mass", DoubleType(), True)
])

# Lire les flux Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "asteroids-topic") \
    .load()

# Convertir et sélectionner les données JSON du message Kafka
structured_df = kafka_df.select(
    from_json(col("value").cast("string"), asteroid_schema).alias("data")
).select("data.*")

# Écrire les données JSON des astéroïdes dans HDFS en format JSON
query = structured_df.writeStream \
    .outputMode("append") \
    .format("json") \
    .option("path", "hdfs://namenode:9000/data/asteroids") \
    .option("checkpointLocation", "hdfs://namenode:9000/checkpoints/asteroids") \
    .start()

# Attendre la fin de la requête
query.awaitTermination()
