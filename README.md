# Projet Asteroid Prediction

## Table des Matières

- [Projet Asteroid Prediction](#projet-asteroid-prediction)
  - [Table des Matières](#table-des-matières)
  - [Introduction](#introduction)
    - [Contexte](#contexte)
    - [Objectifs](#objectifs)
    - [Technologies Utilisées](#technologies-utilisées)
  - [Configuration de l’Environnement](#configuration-de-lenvironnement)
    - [Kafka](#kafka)
    - [Hadoop (HDFS)](#hadoop-hdfs)
    - [Spark](#spark)
  - [Génération de Données](#génération-de-données)
    - [Script de Génération des Données](#script-de-génération-des-données)
  - [Scripts Spark](#scripts-spark)
    - [Script de Nettoyage des données](#script-de-nettoyage-des-données)
  - [Stockage et Traitement des Données](#stockage-et-traitement-des-données)
    - [Stockage dans Hadoop (HDFS)](#stockage-dans-hadoop-hdfs)
    - [Traitement avec Spark](#traitement-avec-spark)
  - [Modélisation Prédictive](#modélisation-prédictive)
    - [Sélection des Algorithmes](#sélection-des-algorithmes)
    - [Entraînement du Modèle](#entraînement-du-modèle)
  - [Visualisation](#visualisation)
    - [Visualisations des Trajectoires](#visualisations-des-trajectoires)
  - [Discussion](#discussion)
    - [Interprétation des Résultats](#interprétation-des-résultats)
    - [Défis Rencontrés](#défis-rencontrés)
    - [Améliorations](#améliorations)
  - [Conclusion](#conclusion)
    - [Résumé](#résumé)
    - [Perspectives Futures](#perspectives-futures)
  - [Annexes](#annexes)
    - [Code Source](#code-source)
    - [Données](#données)
  - [Équipe](#équipe)

---

## Introduction

### Contexte

Ce projet a pour objectif de prédire la probabilité de collision des astéroïdes avec la Terre en utilisant des données simulées et des algorithmes de Machine Learning. Les données des astéroïdes sont générées et publiées sur Kafka, stockées dans HDFS, puis traitées et analysées à l’aide de Spark.

### Objectifs

- Générer des données simulées pour les astéroïdes.
- Stocker et traiter les données avec Hadoop et Spark.
- Développer et évaluer des modèles de prédiction de collision.
- Visualiser les résultats et rédiger un rapport détaillé.

### Technologies Utilisées

- **Kafka** : Pour la gestion des flux de données.
- **Hadoop (HDFS)** : Pour le stockage des données.
- **Spark** : Pour le traitement des données.
- **Python** : Pour la génération des données et le développement des modèles.
- **Scikit-learn, TensorFlow, PyTorch** : Pour la modélisation prédictive.
- **Matplotlib, Seaborn, Plotly** : Pour la visualisation des résultats.

---

## Configuration de l’Environnement

### Kafka

- **Installation** : Suivre la documentation officielle pour installer Kafka sur votre machine ou cluster.
- **Configuration** : Créez un topic pour les données des astéroïdes.

### Hadoop (HDFS)

- **Installation** : Installez Hadoop en suivant la documentation officielle.
- **Configuration** : Configurez HDFS pour le stockage des données.

### Spark

- **Installation** : Installez Apache Spark à partir de la documentation officielle.
- **Configuration** : Assurez-vous que Spark est correctement configuré pour accéder à HDFS et traiter les données.

---

## Génération de Données

### Script de Génération des Données

Lancer le script : 
```bash
python generate_data.py
```



## Scripts Spark

### Script de Nettoyage des données 
```bash
docker exec -it spark-master /bin/bash
```
L'executer depuis le spark master : 
```bash
/spark/bin/spark-submit /app/data_cleaning.py
```

## Stockage et Traitement des Données

### Stockage dans Hadoop (HDFS)

- **Consommateur Kafka** : Configurez un consommateur Kafka pour lire les données des astéroïdes et les stocker dans HDFS.

### Traitement avec Spark

- **Lecture des Données** 
- **Nettoyage des Données**
- **Analyse des Trajectoires** 

## Modélisation Prédictive

### Sélection des Algorithmes

- **Algorithmes Choisis** : Nous avons opté pour la régression logistique en raison de sa simplicité et de son efficacité pour les tâches de classification binaire, telles que la prédiction des collisions d’astéroïdes. La régression logistique est bien adaptée pour modéliser la probabilité d’occurrence d’un événement en fonction des variables d’entrée, ce qui convient parfaitement à notre problème de prédiction de collision.

### Entraînement du Modèle

- **Entraînement** : Les données ont été préparées et nettoyées avant d’être utilisées pour entraîner le modèle. Un pipeline Spark a été créé pour assembler les caractéristiques des astéroïdes en vecteurs de caractéristiques, suivi par un modèle de régression logistique. Nous avons utilisé une séparation de données en ensembles d’entraînement (80%) et de test (20%) pour entraîner le modèle. Le modèle a été entraîné en utilisant PySpark pour tirer parti du traitement distribué.

- **Validation** : La performance du modèle a été évaluée en utilisant l’AUC-ROC comme métrique principale. Un CrossValidator avec une grille de paramètres a été utilisé pour optimiser les hyperparamètres. Les prédictions finales ont été sauvegardées dans HDFS pour une analyse plus approfondie.

## Visualisation

### Visualisations des Trajectoires

- **Graphiques** : ![Trajectoires des Astéroïdes](images/Capture%20d’écran%202024-08-10%20à%2010.46.59.png)
![Trajectoires des Astéroïdes](images/Capture%20d’écran%202024-08-10%20à%2010.46.59.png)



## Discussion

### Interprétation des Résultats

- **Analyse** : Discutez des résultats obtenus à partir des modèles et des visualisations.

### Défis Rencontrés

- **Problèmes** : 
    Collisions Astéroïdes-Terre: Un des défis majeurs a été de ne pas détecter suffisamment de risques de collision avec la Terre. Les valeurs initiales des positions et vitesses des astéroïdes étaient trop élevées, ce qui compliquait l’identification des trajectoires à risque. Pour pallier cela, nous avons ajusté les simulations pour générer des astéroïdes se dirigeant directement vers la Terre. Bien que cette approche soit moins réaliste, elle a permis d’améliorer les visualisations et les modèles prédictifs en créant des cas de test concrets pour mieux évaluer les risques potentiels.

    Problèmes de Docker: L’utilisation de Docker a posé des problèmes de compatibilité et de configuration, nécessitant des ajustements fréquents des fichiers Dockerfile et des paramètres de conteneur pour garantir un environnement stable.

    Versions de Python pour Spark: Des problèmes de compatibilité ont été rencontrés avec Spark, notamment en raison de l’utilisation de différentes versions de Python. Il a fallu synchroniser les versions de Python sur tous les environnements pour assurer le bon fonctionnement des bibliothèques Spark.

    Configuration du PATH Java: La configuration incorrecte du PATH Java a occasionné plusieurs erreurs lors de l’exécution de Spark, nécessitant un ajustement manuel des variables d’environnement pour pointer vers la version correcte de Java.

### Améliorations

- **Amélioration de la Génération de Données** : Enrichir la simulation de données d'astéroïdes avec des modèles physiques plus avancés pour mieux refléter la diversité et les comportements des astéroïdes réels. Cela pourrait inclure des paramètres comme l'effet de la gravité de la Terre sur les trajectoires.

- **Intégration de Données Réelles** : Incorporer des données astronomiques réelles provenant de sources fiables telles que la NASA pour valider et améliorer la précision des modèles de prédiction. Cela aiderait à aligner les simulations avec des scénarios du monde réel.

- **Optimisation des Modèles** : Explorer d'autres algorithmes de machine learning ou de deep learning, tels que les forêts aléatoires ou les réseaux de neurones convolutifs, pour améliorer les performances des prédictions. Utiliser des techniques de fine-tuning pour optimiser davantage les modèles existants.

- **Scalabilité et Performance** : Améliorer la scalabilité du pipeline de données en optimisant l'utilisation de Spark et en explorant des solutions de calcul distribué supplémentaires comme Apache Flink. Cela pourrait permettre de traiter un volume de données plus important plus efficacement.

- **Automatisation des Pipelines** : Mettre en place des pipelines de traitement et d'analyse de données automatisés utilisant des technologies comme Airflow ou Kubeflow. Cela faciliterait l'intégration continue et le déploiement des modèles en production.

- **Visualisations Améliorées** : Développer des visualisations interactives plus avancées, permettant aux utilisateurs d'explorer dynamiquement les trajectoires et les prédictions de collision des astéroïdes. L'utilisation de technologies comme WebGL pourrait enrichir l'expérience utilisateur.

- **Amélioration de l'Interface Utilisateur** : Créer une interface utilisateur conviviale pour visualiser les données et interagir avec les modèles prédictifs, facilitant l'utilisation pour les parties prenantes non techniques.

---

## Conclusion

### Résumé

- **Contributions** : Résumez les principales contributions du projet.

### Perspectives Futures

- **Travail Futur** : 
	•	Amélioration des Modèles : Explorer des modèles avancés, comme les réseaux de neurones profonds, pour améliorer les prédictions de collision.
	•	Intégration de Données Réelles : Utiliser des données astronomiques réelles pour affiner les simulations et accroître le réalisme des résultats.
	•	Optimisation des Performances : Optimiser le traitement des données avec Spark et envisager d’autres solutions comme Apache Flink pour améliorer l’efficacité.
	•	Visualisations Interactives : Améliorer les visualisations interactives pour permettre une exploration plus intuitive des trajectoires et des risques.

---

## Annexes

### Code Source

- **Scripts** : Incluez des liens ou des extraits de code source utilisé dans le projet.

### Données

- **Exemples** : Fournissez des exemples de données utilisées pour les tests et l’entraînement.

## Équipe

Ce projet a été réalisé par :

- Arnaud LAGARDE ([GitHub](https://github.com/arnaudlagarde))
- Pierre-Antoine SAMUEL ([GitHub](https://github.com/PAS2024))
- Nadim HAMIMID ([GitHub](https://github.com/NadimHipssi))