import json
import random
import uuid

# Définir le dictionnaire des planètes
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

# Générer les astéroïdes
num_asteroids = 5000
asteroids = generate_random_asteroids(num_asteroids)

# Créer une liste combinée pour les planètes et les astéroïdes
combined_objects = []

# Ajouter les planètes au format "astéroïde fixe"
for planet_name, position in planets.items():
    planet_as_asteroid = {
        "id": f"planet_{planet_name}",
        "position": position
    }
    combined_objects.append(planet_as_asteroid)

# Ajouter les astéroïdes
combined_objects.extend(asteroids)

# Sauvegarder la liste combinée dans un fichier JSON
with open('combined_objects.json', 'w') as file:
    json.dump(combined_objects, file, indent=4)

print(f"Planètes et {num_asteroids} astéroïdes générés et sauvegardés dans 'combined_objects.json'.")
