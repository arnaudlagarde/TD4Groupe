# Utiliser une image Python de base
FROM python:3.8-slim

# Installer les dépendances nécessaires
RUN pip install kafka-python

# Créer un répertoire pour le code
WORKDIR /producer

# Copier le script du producteur dans le conteneur
COPY producer.py /producer/producer.py

# Copier le script generate_data.py depuis l'extérieur du répertoire producer
COPY generate_data.py /producer/generate_data.py

# Définir la commande par défaut pour exécuter le producteur Kafka
CMD ["python", "/producer/producer.py"]
