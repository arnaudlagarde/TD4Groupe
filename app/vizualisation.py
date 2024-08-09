from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sqrt, pow
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize Spark Session
spark = SparkSession.builder.appName("Asteroid Collision Visualization").getOrCreate()

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

# Simulate asteroid positions
simulated_df = simulate_trajectories(filtered_df, total_days)

# Calculate distance to Earth
simulated_df = simulated_df.withColumn("distance_to_earth",
                                       sqrt(pow(col("position.x") - 1.496e8, 2) +  # 1 AU in km
                                            pow(col("position.y"), 2) +
                                            pow(col("position.z"), 2)))

# Determine collision risk
collision_risk_df = simulated_df.withColumn("collision_risk",
                                            col("distance_to_earth") < collision_threshold_km)

# Collect data for visualization
positions = collision_risk_df.select("id", "position.x", "position.y", "position.z", "collision_risk").collect()

# Prepare data for plotting
ids = [row['id'] for row in positions]
x_positions = [row['x'] for row in positions]
y_positions = [row['y'] for row in positions]
z_positions = [row['z'] for row in positions]
collision_risks = [row['collision_risk'] for row in positions]

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot all asteroids
ax.scatter(x_positions, y_positions, z_positions, c='blue', label='Asteroids')

# Highlight potential collisions
collision_indices = [i for i, risk in enumerate(collision_risks) if risk]
ax.scatter([x_positions[i] for i in collision_indices],
           [y_positions[i] for i in collision_indices],
           [z_positions[i] for i in collision_indices], 
           c='red', label='Potential Collision')

# Label the plot
ax.set_title('Asteroid Trajectories and Collision Predictions')
ax.set_xlabel('X Position (km)')
ax.set_ylabel('Y Position (km)')
ax.set_zlabel('Z Position (km)')
ax.legend()

# Show plot
plt.show()

# Generate a simple report
total_asteroids = len(positions)
potential_collisions = len(collision_indices)

print(f"Total Asteroids Analyzed: {total_asteroids}")
print(f"Potential Collisions: {potential_collisions}")
print(f"Details of Potential Collisions: {[ids[i] for i in collision_indices]}")

# Stop the Spark session
spark.stop()