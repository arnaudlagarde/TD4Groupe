from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    max as spark_max,
    min as spark_min,
    mean,
    count,
    window,
    when,
    stddev,
    corr,
    lag,
    unix_timestamp,
)
from pyspark.sql.window import Window

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("ComprehensiveSeismicAnalysis") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Load the cleaned seismic data from HDFS in Parquet format
seismic_df = spark.read.parquet("hdfs://namenode:9000/data/cleaned/cleaned_seismic_data")

# Load the city data from HDFS in Parquet format
city_df = spark.read.parquet("hdfs://namenode:9000/data/cities")

# Convert necessary columns to appropriate types
seismic_data = seismic_df.withColumn("magnitude", col("magnitude").cast("double")) \
                         .withColumn("tension entre plaque", col("tension entre plaque").cast("double")) \
                         .withColumn("date", col("date").cast("timestamp"))

city_data = city_df.withColumn("date", col("date").cast("timestamp")) \
                   .withColumn("magnitude", col("magnitude").cast("double"))

# Join the datasets on the date column
joined_data = seismic_data.join(city_data, "date")

# Display schema and first few rows for inspection
joined_data.printSchema()
joined_data.show(5)

# Basic Statistics
print("=== Basic Statistics ===")
joined_data.describe().show()

# Calculate the amplitude over a daily basis for each city
window_spec = window(col("date"), "1 day")
city_seismic_amplitude = joined_data.groupBy("ville", window_spec).agg(
    spark_max("magnitude").alias("max_magnitude"),
    spark_min("magnitude").alias("min_magnitude"),
    mean("magnitude").alias("mean_magnitude"),
    count("magnitude").alias("count_magnitude")
).withColumn("amplitude", col("max_magnitude") - col("min_magnitude"))

# Identify significant seismic activities by city
significant_threshold = 2.0
significant_city_activity = city_seismic_amplitude.filter(col("amplitude") > significant_threshold)

print("=== Significant Seismic Activity by City ===")
significant_city_activity.show()

# Correlation Analysis
print("=== Correlation Analysis ===")
# Calculate correlation between magnitude and tension for each city
city_correlations = joined_data.groupBy("ville").agg(
    corr("magnitude", "tension entre plaque").alias("correlation_magnitude_tension")
)

print("=== Correlations by City ===")
city_correlations.show()

# Time-based correlation - lag analysis for each city
window_spec_lag = Window.partitionBy("ville").orderBy("date")
joined_data = joined_data.withColumn("lag_magnitude", lag("magnitude", 1).over(window_spec_lag))

# Difference in magnitude between consecutive readings for each city
joined_data = joined_data.withColumn("magnitude_diff", col("magnitude") - col("lag_magnitude"))

# Calculate correlation between tension and magnitude_diff for each city
city_diff_correlations = joined_data.groupBy("ville").agg(
    corr("tension entre plaque", "magnitude_diff").alias("correlation_tension_magnitude_diff")
)

print("=== Correlations of Tension and Magnitude Difference by City ===")
city_diff_correlations.show()

# Frequency Analysis of Seismic Events by City
print("=== Frequency Analysis of Seismic Events by City ===")
# Define threshold for classifying an event as a seismic activity
seismic_event_threshold = 1.5
joined_data = joined_data.withColumn("is_seismic_event", when(col("magnitude") > seismic_event_threshold, 1).otherwise(0))

# Count of seismic events per day by city
city_seismic_event_count = joined_data.groupBy("ville", window_spec).agg(
    count(when(col("is_seismic_event") == 1, 1)).alias("seismic_event_count")
)

print("=== Seismic Event Count per Day by City ===")
city_seismic_event_count.show()

# Analyze trends over time by city
print("=== Trend Analysis by City ===")
# Calculate rolling average of magnitude for each city
window_spec_rolling = Window.partitionBy("ville").orderBy("date").rowsBetween(-7, 0)  # 7-day rolling window
joined_data = joined_data.withColumn("rolling_avg_magnitude", mean("magnitude").over(window_spec_rolling))

# Display trend data by city
city_trend_data = joined_data.select("date", "ville", "magnitude", "rolling_avg_magnitude")
city_trend_data.show()

# Save significant seismic activity and trends to HDFS in Parquet format
significant_city_activity.write.parquet("hdfs://namenode:9000/data/significant_city_activity", mode="overwrite")
city_trend_data.write.parquet("hdfs://namenode:9000/data/city_trend_analysis", mode="overwrite")

# Stop the Spark session
spark.stop()
