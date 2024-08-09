from kafka import KafkaProducer
import json
import time
from generate_data import generate_asteroid_data  # Importer la fonction

# Configurer le producteur Kafka
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Envoyer les données d'astéroïdes à Kafka
def send_data_to_kafka():
    while True:
        data = generate_asteroid_data()  # Utilisation de la fonction importée
        producer.send('asteroids-topic', value=data)
        print(f"Sent data: {data}")
        time.sleep(1)  # Envoie un message toutes les secondes

if __name__ == "__main__":
    send_data_to_kafka()
