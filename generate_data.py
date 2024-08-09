import json
import random
import uuid

# Dictionnaire des planètes réalistes (en millions de km)
planets = {
    "Mercure": {"x": 57900000.0, "y": 0.0, "z": 0.0},
    "Venus": {"x": 108200000.0, "y": 0.0, "z": 0.0},
    "Terre": {"x": 149600000.0, "y": 0.0, "z": 0.0},
    "Mars": {"x": 227900000.0, "y": 0.0, "z": 0.0},
    "Jupiter": {"x": 778600000.0, "y": 0.0, "z": 0.0},
    "Saturne": {"x": 1433500000.0, "y": 0.0, "z": 0.0},
    "Uranus": {"x": 2872500000.0, "y": 0.0, "z": 0.0},
    "Neptune": {"x": 4495100000.0, "y": 0.0, "z": 0.0},
    "Pluton": {"x": 5913000000.0, "y": 0.0, "z": 0.0}
}

# Sauvegarder le dictionnaire des planètes dans un fichier JSON
with open('planets.json', 'w') as file:
    json.dump(planets, file, indent=4)

print("Dictionnaire des planètes sauvegardé dans 'planets.json'.")

# Fonction pour générer des données aléatoires pour les astéroïdes
def generate_random_asteroids(num_asteroids):
    asteroids = []
    for i in range(num_asteroids):
        asteroid = {
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
        asteroids.append(asteroid)
    return asteroids

# Générer 5000 astéroïdes
num_asteroids = 5000
asteroids = generate_random_asteroids(num_asteroids)

with open('asteroids.json', 'w') as file:
    json.dump(asteroids, file, indent=4)

print(f"{num_asteroids} astéroïdes générés et sauvegardés dans 'asteroids.json'.")