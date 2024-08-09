import json
import uuid
import random

def generate_asteroid_data():
    asteroid_data = {
        "id": f"asteroid_{str(uuid.uuid4())}",
        "position": {
            "x": random.uniform(-1e7, 1e7),
            "y": random.uniform(-1e7, 1e7),
            "z": random.uniform(-1e7, 1e7)
        },
        "velocity": {
            "vx": random.uniform(-100.0, 100.0),
            "vy": random.uniform(-100.0, 100.0),
            "vz": random.uniform(-100.0, 100.0)
        },
        "size": random.uniform(0.1, 10.0),
        "mass": random.uniform(1e10, 1e15)
    }
    return asteroid_data

if __name__ == "__main__":
    data = generate_asteroid_data()
    print(json.dumps(data, indent=4))
