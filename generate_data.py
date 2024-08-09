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

# Générer 5000 astéroïdes et les sauvegarder dans un fichier JSON
num_asteroids = 5000
asteroids = generate_random_asteroids(num_asteroids)

# Liste des noms des planètes pour les associer aux astéroïdes
planet_names = list(planets.keys())

# Créer une liste pour stocker les couples planète-astéroïde
combined_objects = []

# Associer chaque astéroïde à une planète
for i in range(num_asteroids):
    planet_name = planet_names[i % len(planet_names)]  # Sélectionne la planète de manière cyclique
    planet_position = planets[planet_name]
    
    combined_object = {
        "asteroid": asteroids[i],
        "planet": {
            "name": planet_name,
            "position": planet_position
        }
    }
    combined_objects.append(combined_object)

# Sauvegarder la liste combinée dans un fichier JSON
with open('combined_asteroids_planets.json', 'w') as file:
    json.dump(combined_objects, file, indent=4)

print(f"{num_asteroids} couples astéroïde-planète générés et sauvegardés dans 'combined_asteroids_planets.json'.")