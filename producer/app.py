import pandas as pd
from kafka import KafkaProducer
import json

# Configurations
csv_file_1 = "../data/dataset_sismique.csv"  
csv_file_2 = "../data/dataset_sismique_villes.csv"  
topic_name_1 = "topic1"  
topic_name_2 = "topic2"

# Initialiser le producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_csv_to_kafka(file_path, topic):
    # Lire le CSV
    data = pd.read_csv(file_path)
    
    # Envoyer les données à Kafka
    for _, row in data.iterrows():
        message = row.to_dict()
        producer.send(topic, value=message)
        print(f"Sent from {file_path}: {message}")

# Envoyer les données du premier CSV
send_csv_to_kafka(csv_file_1, topic_name_1)

# Envoyer les données du deuxième CSV
send_csv_to_kafka(csv_file_2, topic_name_2)

# Fermer le producteur
producer.close()
