from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    max as spark_max,
    min as spark_min,
    mean,
    count,
    window,
)

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("PreliminarySeismicAnalysis") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Load the cleaned seismic data from HDFS in Parquet format
df = spark.read.parquet("hdfs://namenode:9000/data/cleaned/cleaned_seismic_data")

# Convert necessary columns to appropriate types
seismic_data = df.withColumn("magnitude", col("magnitude").cast("double")) \
                 .withColumn("tension entre plaque", col("tension entre plaque").cast("double")) \
                 .withColumn("date", col("date").cast("timestamp"))

# Display schema and first few rows for inspection
seismic_data.printSchema()
seismic_data.show(5)

# Calculate the amplitude over a daily basis
window_spec = window(col("date"), "1 day")
seismic_with_amplitude = seismic_data.groupBy(window_spec).agg(
    spark_max("magnitude").alias("max_magnitude"),
    spark_min("magnitude").alias("min_magnitude"),
    mean("magnitude").alias("mean_magnitude"),
    count("magnitude").alias("count_magnitude")
).withColumn("amplitude", col("max_magnitude") - col("min_magnitude"))

# Identify significant seismic activities
significant_threshold = 2.0  # Example threshold for significance
significant_seismic_activity = seismic_with_amplitude.filter(col("amplitude") > significant_threshold)

print("=== Significant Seismic Activity ===")
significant_seismic_activity.show()

# Save significant seismic activity to HDFS in Parquet format
significant_seismic_activity.write.parquet("hdfs://namenode:9000/data/significant_seismic_activity", mode="overwrite")

# Stop the Spark session
spark.stop()
