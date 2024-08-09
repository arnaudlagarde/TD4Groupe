from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, isnan, round
from pyspark.sql.types import DoubleType

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Asteroid Data Cleaning") \
    .master("local[*]") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

# Load data from HDFS
# df = spark.read.json("hdfs://namenode:9000/data/combined_objects.ndjson")
df = spark.read.json("hdfs://namenode:9000/data/asteroids/*.json")

# Display the initial DataFrame structure
df.printSchema()

# Initial data inspection
df.show(5, truncate=False)
df.describe().show()

# Drop rows with any null values in critical columns
df_clean = df.dropna(subset=["mass", "size", "position", "velocity"])

# Filtering out invalid or extreme values
# Ensure all numeric fields have realistic bounds

# Clean mass: removing invalid entries (negative or unrealistic values)
df_clean = df_clean.filter((col("mass") > 0) & (col("mass") < 1e16))  # Example bound for mass

# Clean size: removing unrealistic sizes
size_threshold_min = 0.1  # Example minimum threshold for size
size_threshold_max = 100.0  # Example maximum threshold for size
df_clean = df_clean.filter((col("size") >= size_threshold_min) & (col("size") <= size_threshold_max))

# Validate positions: ensuring values are within a realistic range
df_clean = df_clean.filter((col("position.x").between(-1e8, 1e8)) &
                           (col("position.y").between(-1e8, 1e8)) &
                           (col("position.z").between(-1e8, 1e8)))

# Validate velocities: ensuring values are within a realistic range
velocity_threshold = 1e3  # Example threshold for velocity
df_clean = df_clean.filter((col("velocity.vx").between(-velocity_threshold, velocity_threshold)) &
                           (col("velocity.vy").between(-velocity_threshold, velocity_threshold)) &
                           (col("velocity.vz").between(-velocity_threshold, velocity_threshold)))

# Handling outliers: applying statistical methods (optional)
# Example: capping outliers using quantile-based flooring and capping
quantiles = df_clean.approxQuantile(["mass", "size"], [0.01, 0.99], 0.05)
df_clean = df_clean.withColumn("mass", when(col("mass") < quantiles[0][0], quantiles[0][0]).otherwise(col("mass")))
df_clean = df_clean.withColumn("mass", when(col("mass") > quantiles[0][1], quantiles[0][1]).otherwise(col("mass")))

df_clean = df_clean.withColumn("size", when(col("size") < quantiles[1][0], quantiles[1][0]).otherwise(col("size")))
df_clean = df_clean.withColumn("size", when(col("size") > quantiles[1][1], quantiles[1][1]).otherwise(col("size")))

# Rounding off numerical columns for consistency
df_final = df_clean.withColumn("mass", round(col("mass"), 2)) \
                   .withColumn("size", round(col("size"), 2)) \
                   .withColumn("position.x", round(col("position.x"), 2)) \
                   .withColumn("position.y", round(col("position.y"), 2)) \
                   .withColumn("position.z", round(col("position.z"), 2)) \
                   .withColumn("velocity.vx", round(col("velocity.vx"), 2)) \
                   .withColumn("velocity.vy", round(col("velocity.vy"), 2)) \
                   .withColumn("velocity.vz", round(col("velocity.vz"), 2))

# Selecting necessary columns
df_final = df_final.select("id", "position", "velocity", "size", "mass")

# Show the result after cleaning
df_final.show()

# Save the cleaned data back to HDFS
df_final.write.mode("overwrite").json("hdfs://namenode:9000/data/cleaned_data.json")

# Stop the Spark session
spark.stop()