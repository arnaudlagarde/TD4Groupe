import json
import random

def generate_asteroid_data(num_asteroids=1000):
    asteroids = []
    for i in range(num_asteroids):
        asteroid = {
            "id": f"asteroid_{str(i).zfill(3)}",
            "position": {
                "x": random.uniform(100000, 500000),  # Position x entre 100 000 et 500 000
                "y": random.uniform(-200000, 200000), # Position y entre -200 000 et 200 000
                "z": random.uniform(-100000, 100000)  # Position z entre -100 000 et 100 000
            },
            "velocity": {
                "vx": random.uniform(-50, 50),  # Vitesse vx entre -50 et 50
                "vy": random.uniform(-50, 50),  # Vitesse vy entre -50 et 50
                "vz": random.uniform(-50, 50)   # Vitesse vz entre -50 et 50
            },
            "size": round(random.uniform(0.1, 10.0), 2),  # Taille en kilomètres
            "mass": round(random.uniform(1e10, 1e15), 2)  # Masse en kilogrammes
        }
        asteroids.append(asteroid)
    return asteroids

# Générer des données pour 10 astéroïdes
asteroid_data = generate_asteroid_data(1000)

# Sauvegarder les données dans un fichier JSON
with open('data/asteroids_more_realistic.json', 'w') as f:
    json.dump(asteroid_data, f, indent=2)

print(json.dumps(asteroid_data, indent=2))  # Afficher les données générées