from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sqrt, pow
import json

# Create a Spark session
spark = SparkSession.builder \
    .appName("Asteroid Trajectory and Collision Probability") \
    .getOrCreate()

# Load the combined NDJSON data
file_path = "hdfs://namenode:9000/data/combined_objects.ndjson"
data_df = spark.read.json(file_path)

# Filter out planets and prepare asteroids DataFrame
asteroids_df = data_df.filter(~col("id").like("planet_%"))

# Simulate asteroid trajectories over multiple days
def simulate_asteroid_trajectories(df, days):
    seconds_in_day = 86400
    for day in range(days):
        df = df.withColumn(
            "position.x",
            col("position.x") + col("velocity.vx") * seconds_in_day
        ).withColumn(
            "position.y",
            col("position.y") + col("velocity.vy") * seconds_in_day
        ).withColumn(
            "position.z",
            col("position.z") + col("velocity.vz") * seconds_in_day
        )
        print(f"Simulated Day {day + 1}:")
        df.select("id", "position.x", "position.y", "position.z").show(5)
    return df

# Run simulation for 30 days (or more)
asteroids_future_df = simulate_asteroid_trajectories(asteroids_df, 30)

# Calculate distance to Earth and potential collision risk
def calculate_collision_risk(df):
    # Constants for Earth's position
    earth_x, earth_y, earth_z = 149600000.0, 0.0, 0.0
    collision_distance_threshold = 1e7  # 10,000,000 km

    # Calculate distance to Earth
    with_distance_df = df.withColumn(
        "distance_to_earth",
        sqrt(
            pow(col("position.x") - earth_x, 2) +
            pow(col("position.y") - earth_y, 2) +
            pow(col("position.z") - earth_z, 2)
        )
    )

    # Determine collision risk
    collision_risk_df = with_distance_df.withColumn(
        "collision_risk",
        col("distance_to_earth") < collision_distance_threshold
    )

    # Display potential collision risks
    collision_risk_df.select(
        "id", "mass", "size", "distance_to_earth", "collision_risk"
    ).filter(col("collision_risk") == True).show(5)

    return collision_risk_df

# Apply collision risk calculations
collision_risk_df = calculate_collision_risk(asteroids_future_df)

# Select and display asteroids with potential collision risk
potential_collisions_df = collision_risk_df.select(
    col("id"),
    col("mass").alias("mass (kg)"),
    col("size").alias("size (m)"),
    col("distance_to_earth").alias("Distance to Earth (km)"),
    col("collision_risk")
).filter(col("collision_risk") == True)

print("Asteroids with Potential Collision Risk:")
potential_collisions_df.show(10)

# Save results back to HDFS
output_path = "hdfs://namenode:9000/data/asteroid_trajectories.ndjson"
potential_collisions_df.write.json(output_path, mode='overwrite')

# Stop the Spark session
spark.stop()