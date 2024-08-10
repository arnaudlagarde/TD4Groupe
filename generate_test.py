import json
import random
import uuid

def generate_asteroids(num_asteroids):
    asteroids = []
    for i in range(num_asteroids):
        if i < 500:  # Increase the number of close and fast-moving asteroids
            # Position very close to Earth, within 1,000,000 km
            x = random.uniform(148.6e6, 150.6e6)
            y = random.uniform(-1e5, 1e5)
            z = random.uniform(-1e5, 1e5)
            # Higher velocity towards Earth
            vx = -x / (50 * 365.25 * 24 * 3600)  # Adjust velocity to reach Earth in about 50 years
            vy = -y / (50 * 365.25 * 24 * 3600)
            vz = -z / (50 * 365.25 * 24 * 3600)
        else:
            # Position generally around the solar system
            x = random.uniform(-1e8, 1e8) + 149600000
            y = random.uniform(-1e8, 1e8)
            z = random.uniform(-1e8, 1e8)
            # Regular velocity towards Earth
            vx = -x / (random.uniform(300, 700) * 365.25 * 24 * 3600)
            vy = -y / (random.uniform(300, 700) * 365.25 * 24 * 3600)
            vz = -z / (random.uniform(300, 700) * 365.25 * 24 * 3600)

        asteroid = {
            "id": f"asteroid_{str(uuid.uuid4())}",
            "position": {"x": x, "y": y, "z": z},
            "velocity": {"vx": vx, "vy": vy, "vz": vz},
            "size": random.uniform(0.1, 10.0),
            "mass": random.uniform(1e10, 1e15)
        }
        asteroids.append(asteroid)

    return asteroids

num_asteroids = 100000
asteroids = generate_asteroids(num_asteroids)

with open('data/asteroids.json', 'w') as file:
    json.dump(asteroids, file, indent=4)

print(f"Generated and saved {num_asteroids} asteroids in 'asteroids.json'.")