from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sqrt, pow

# Initialize Spark Session
spark = SparkSession.builder.appName("Asteroid Collision Detection").getOrCreate()

# Load your dataset into a DataFrame
asteroids_df = spark.read.json("hdfs://namenode:9000/data/combined_objects.ndjson")

# Verify Data Fields
print("Verifying Data Fields:")
asteroids_df.printSchema()
asteroids_df.show(5)

# Define simulation parameters
years_to_simulate = 5  # Simulate for 5 years
days_per_year = 365  # Days in a year
total_days = years_to_simulate * days_per_year
collision_threshold_km = 1e5  # Adjust collision threshold to 100,000 km

# Function to simulate trajectories
def simulate_trajectories(df, days):
    # Update positions based on velocity and duration
    return df.withColumn("position.x", col("position.x") + col("velocity.vx") * days) \
             .withColumn("position.y", col("position.y") + col("velocity.vy") * days) \
             .withColumn("position.z", col("position.z") + col("velocity.vz") * days)

# Filter out any null velocity values
filtered_df = asteroids_df.filter(col("velocity.vx").isNotNull() &
                                  col("velocity.vy").isNotNull() &
                                  col("velocity.vz").isNotNull())

print("Filtered Data with Non-null Velocities:")
filtered_df.show(5)

# Simulate asteroid positions
simulated_df = simulate_trajectories(filtered_df, total_days)

print(f"Simulated Data after {total_days} days:")
simulated_df.select("id", "position", "velocity").show(5)

# Calculate distance to Earth
simulated_df = simulated_df.withColumn("distance_to_earth",
                                       sqrt(pow(col("position.x") - 1.496e8, 2) +  # 1 AU in km
                                            pow(col("position.y"), 2) +
                                            pow(col("position.z"), 2)))

print("Data with Calculated Distance to Earth:")
simulated_df.select("id", "distance_to_earth").show(5)

# Determine collision risk
collision_risk_df = simulated_df.withColumn("collision_risk",
                                            col("distance_to_earth") < collision_threshold_km)

print(f"Asteroids with Distance < {collision_threshold_km} km:")
collision_risk_df.filter(col("collision_risk") == True).select("id", "distance_to_earth").show(10)

# Select and display potential collisions
potential_collisions_df = collision_risk_df.select(
    col("id"),
    col("mass").alias("mass (kg)"),
    col("size").alias("size (m)"),
    col("distance_to_earth").alias("Distance to Earth (km)"),
    col("collision_risk")
).filter(col("collision_risk") == True)

# Show asteroids with potential collision risk
print("Asteroids with Potential Collision Risk:")
potential_collisions_df.show(10)

# Stop the Spark session
spark.stop()