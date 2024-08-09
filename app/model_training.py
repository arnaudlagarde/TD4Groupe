from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml import Pipeline

# Initialiser la session Spark
spark = SparkSession.builder \
    .appName("Asteroid Model Training") \
    .getOrCreate()

# Charger les données préparées depuis HDFS
df = spark.read.json("hdfs://namenode:9000/data/cleaned_prepared_data")

# Assembler les features en un vecteur
assembler = VectorAssembler(inputCols=["velocity.vx", "velocity.vy", "velocity.vz", "size", "mass", "distance_to_earth"], outputCol="features")
df = assembler.transform(df)

# Séparer les données en ensembles d'entraînement et de test
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Initialiser le modèle de régression logistique
lr = LogisticRegression(labelCol="collision", featuresCol="features")

# Pipeline
pipeline = Pipeline(stages=[assembler, lr])

# Entraîner le modèle
model = pipeline.fit(train_data)

# Évaluer le modèle sur l'ensemble de test
predictions = model.transform(test_data)
evaluator = BinaryClassificationEvaluator(labelCol="collision", rawPredictionCol="rawPrediction")
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")

# Sauvegarder le modèle
model.write().overwrite().save("hdfs://namenode:9000/model/asteroid_collision_model")

# Arrêter la session Spark
spark.stop()
