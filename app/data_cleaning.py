from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, stddev
from pyspark.sql.types import DoubleType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SeismicDataCleaning") \
    .getOrCreate()

# Read seismic data from HDFS (Parquet format)
df_seismic = spark.read.parquet("hdfs://namenode:9000/data/seismic")
df_cities = spark.read.parquet("hdfs://namenode:9000/data/cities")

# Drop duplicates
df_seismic = df_seismic.dropDuplicates()
df_cities = df_cities.dropDuplicates()

# Clean seismic data: Drop rows with null or NaN values in critical columns
df_seismic_cleaned = df_seismic.na.drop(subset=["magnitude", "tension entre plaque"])
df_cities_cleaned = df_cities.na.drop(subset=["magnitude", "tension entre plaque"])

# Convert columns to correct data types if necessary
df_seismic_cleaned = df_seismic_cleaned.withColumn("magnitude", col("magnitude").cast(DoubleType()))
df_seismic_cleaned = df_seismic_cleaned.withColumn("tension entre plaque", col("tension entre plaque").cast(DoubleType()))

df_cities_cleaned = df_cities_cleaned.withColumn("magnitude", col("magnitude").cast(DoubleType()))
df_cities_cleaned = df_cities_cleaned.withColumn("tension entre plaque", col("tension entre plaque").cast(DoubleType()))

# Identify and remove outliers using statistical methods
mean_magnitude = df_seismic_cleaned.select(avg(col("magnitude"))).first()[0]
stddev_magnitude = df_seismic_cleaned.select(stddev(col("magnitude"))).first()[0]

# Filter out outliers based on a threshold, e.g., 3 standard deviations
df_seismic_cleaned = df_seismic_cleaned.filter(
    (col("magnitude") >= mean_magnitude - 3 * stddev_magnitude) &
    (col("magnitude") <= mean_magnitude + 3 * stddev_magnitude)
)

# Rename columns in df_cities_cleaned to avoid conflicts
df_cities_cleaned = df_cities_cleaned.withColumnRenamed("magnitude", "city_magnitude") \
                                     .withColumnRenamed("secousse", "city_secousse") \
                                     .withColumnRenamed("tension entre plaque", "city_tension_entre_plaque")

# Join datasets on the date column
df_joined = df_seismic_cleaned.join(df_cities_cleaned, on="date", how="inner")

# Save the cleaned and joined data to HDFS (as Parquet)
df_joined.write.parquet("hdfs://namenode:9000/data/cleaned/cleaned_seismic_data", mode="overwrite")

# Stop the Spark session
spark.stop()
