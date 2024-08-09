from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    avg,
    sum as spark_sum,
    count,
    window,
    year,
    month,
    weekofyear,
    dayofweek,
    to_date,
)

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("SeismicDataAggregation") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Load the cleaned seismic data from HDFS in Parquet format
seismic_data = spark.read.parquet("hdfs://namenode:9000/data/cleaned/cleaned_seismic_data")

# Convert necessary columns to appropriate types
seismic_data = seismic_data.withColumn("magnitude", col("magnitude").cast("double")) \
                           .withColumn("tension entre plaque", col("tension entre plaque").cast("double")) \
                           .withColumn("date", col("date").cast("timestamp"))

# Aggregation Functions

# 1. Daily Aggregation
daily_aggregation = seismic_data.groupBy(to_date(col("date")).alias("date")).agg(
    avg("magnitude").alias("avg_magnitude"),
    spark_sum("magnitude").alias("sum_magnitude"),
    count("magnitude").alias("count_magnitude")
)

# 2. Weekly Aggregation
weekly_aggregation = seismic_data.groupBy(year("date").alias("year"), weekofyear("date").alias("week")).agg(
    avg("magnitude").alias("avg_magnitude"),
    spark_sum("magnitude").alias("sum_magnitude"),
    count("magnitude").alias("count_magnitude")
)

# 3. Monthly Aggregation
monthly_aggregation = seismic_data.groupBy(year("date").alias("year"), month("date").alias("month")).agg(
    avg("magnitude").alias("avg_magnitude"),
    spark_sum("magnitude").alias("sum_magnitude"),
    count("magnitude").alias("count_magnitude")
)

# 4. Seasonal Aggregation (By Day of the Week)
seasonal_aggregation = seismic_data.groupBy(dayofweek("date").alias("day_of_week")).agg(
    avg("magnitude").alias("avg_magnitude"),
    spark_sum("magnitude").alias("sum_magnitude"),
    count("magnitude").alias("count_magnitude")
)

# Display Aggregated Data
print("=== Daily Aggregation ===")
daily_aggregation.show()

print("=== Weekly Aggregation ===")
weekly_aggregation.show()

print("=== Monthly Aggregation ===")
monthly_aggregation.show()

print("=== Seasonal Aggregation ===")
seasonal_aggregation.show()

# Save aggregated data to HDFS in Parquet format
daily_aggregation.write.parquet("hdfs://namenode:9000/data/daily_aggregation", mode="overwrite")
weekly_aggregation.write.parquet("hdfs://namenode:9000/data/weekly_aggregation", mode="overwrite")
monthly_aggregation.write.parquet("hdfs://namenode:9000/data/monthly_aggregation", mode="overwrite")
seasonal_aggregation.write.parquet("hdfs://namenode:9000/data/seasonal_aggregation", mode="overwrite")

# Stop the Spark session
spark.stop()
