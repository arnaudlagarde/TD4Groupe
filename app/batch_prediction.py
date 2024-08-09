from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

# Initialiser la session Spark
spark = SparkSession.builder \
    .appName("Asteroid Batch Prediction") \
    .getOrCreate()

# Charger le modèle
model = PipelineModel.load("hdfs://namenode:9000/model/asteroid_collision_model")

# Charger les nouvelles données des astéroïdes
new_data = spark.read.json("hdfs://namenode:9000/data/new_asteroids/*.json")

# Appliquer le modèle pour faire des prédictions
predictions = model.transform(new_data)

# Sauvegarder les prédictions
predictions.select("id", "prediction").write.mode("overwrite").json("hdfs://namenode:9000/data/predicted_collisions")

# Arrêter la session Spark
spark.stop()
