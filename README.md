# Projet Asteroid Prediction

## Table des Matières

- [Projet Asteroid Prediction](#projet-asteroid-prediction)
  - [Table des Matières](#table-des-matières)
  - [Introduction](#introduction)
    - [Contexte](#contexte)
    - [Objectifs](#objectifs)
    - [Technologies Utilisées](#technologies-utilisées)
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
    - [Analyse des Approches les Plus Proches](#analyse-des-approches-les-plus-proches)
    - [Défis Rencontrés](#défis-rencontrés)
    - [Améliorations](#améliorations)
  - [Conclusion](#conclusion)
    - [Perspectives Futures](#perspectives-futures)
  - [Annexes](#annexes)
    - [Code Source](#code-source)
    - [Données](#données)
  - [Équipe](#équipe)

---

## Introduction

### Contexte

Ce projet a pour objectif de prédire la probabilité de collision des astéroïdes avec la Terre en utilisant des données simulées et des algorithmes de Machine Learning. Les données des astéroïdes sont générées et publiées sur Kafka, stockées dans HDFS, puis traitées et analysées à l’aide de Spark et visualiser avec Matplotlib.

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

- **Algorithmes Choisis** : Nous avons opté pour la régression logistique en raison de sa simplicité et de son efficacité pour les tâches de classification binaire, telles que la prédiction des collisions d’astéroïdes. Cela convient parfaitement à notre problème de prédiction de collision.

### Entraînement du Modèle

- **Entraînement** : Les données ont été préparées et nettoyées avant d’être utilisées pour entraîner le modèle. Un pipeline Spark a été créé pour assembler les caractéristiques des astéroïdes en vecteurs de caractéristiques, suivi par un modèle de régression logistique. Nous avons utilisé une séparation de données en ensembles d’entraînement (80%) et de test (20%) pour entraîner le modèle. Le modèle a été entraîné en utilisant PySpark pour tirer parti du traitement distribué.

- **Validation** : La performance du modèle a été évaluée en utilisant l’AUC-ROC comme métrique principale. Un CrossValidator avec une grille de paramètres a été utilisé pour optimiser les hyperparamètres. Les prédictions finales ont été sauvegardées dans HDFS pour une analyse plus approfondie.

## Visualisation

### Visualisations des Trajectoires

- **Graphiques** : 

![Trajectoires des Astéroïdes](images/Capture%20d’écran%202024-08-10%20à%2010.46.59.png)
![Trajectoires des Astéroïdes](images/Capture%20d’écran%202024-08-10%20à%2010.46.59.png)


## Discussion

### Interprétation des Résultats

Les simulations ont mis en évidence des trajectoires d'astéroïdes qui se rapprochent de la Terre, soulignant l'efficacité de notre modèle pour identifier les risques potentiels. Les résultats montrent que certains astéroïdes passent près de la Terre, justifiant une surveillance continue pour anticiper des mesures de déviation. Les visualisations en trois dimensions offrent une perspective claire sur ces approches, essentielle pour les planificateurs et les chercheurs.

### Analyse des Approches les Plus Proches

Plusieurs astéroïdes s'approchent à des distances critiques, comme l'astéroïde `asteroid_fdba38c6-c025-4d62-b6d1-1503f9b5f2b4` avec une proximité de 11,561 km dans une dizaine d'année (ce sont de fausses données et nous avons fait en sorte que cela se produise). 


### Défis Rencontrés

- **Problèmes** : 
    Collisions Astéroïdes-Terre: Un des défis majeurs a été de ne pas détecter suffisamment de risques de collision avec la Terre. Les valeurs initiales des positions et vitesses des astéroïdes étaient trop élevées, ce qui compliquait l’identification des trajectoires à risque. Pour pallier cela, nous avons ajusté les simulations pour générer des astéroïdes se dirigeant directement vers la Terre. Bien que cette approche soit moins réaliste, elle a permis d’améliorer les visualisations et les modèles prédictifs en créant des cas de test concrets pour mieux évaluer les risques potentiels.

    Problèmes de Docker: L’utilisation de Docker a posé des problèmes de compatibilité et de configuration, nécessitant des ajustements fréquents des fichiers Dockerfile et des paramètres de conteneur pour garantir un environnement stable.

    Versions de Python pour Spark: Des problèmes de compatibilité ont été rencontrés avec Spark, notamment en raison de l’utilisation de différentes versions de Python. Il a fallu synchroniser les versions de Python sur tous les environnements pour assurer le bon fonctionnement des bibliothèques Spark.

    Configuration du PATH Java: La configuration incorrecte du PATH Java a occasionné plusieurs erreurs lors de l’exécution de Spark, nécessitant un ajustement manuel des variables d’environnement pour pointer vers la version correcte de Java.

    Travail collaboratif : Difficile de se répartir les tâches en sachant que le travail de l'un est nécessaire pour l'autre qui ne peut rien faire pendant ce temps là.

### Améliorations

- **Amélioration de la Génération de Données** : Enrichir la simulation de données d'astéroïdes avec des modèles physiques plus avancés pour mieux refléter la diversité et les comportements des astéroïdes réels. Effet de la gravité de la Terre sur les trajectoires etc...

- **Intégration de Données Réelles** : Incorporer des données astronomiques réelles provenant de sources fiables telles que la NASA pour valider et améliorer la précision des modèles de prédiction. Cela aiderait à aligner les simulations avec des scénarios du monde réel. - La génération d'astéroïdes a été faite un peu vite ce qui nous a causé de nombreux problèmes lors de la Visualisation et la réalisation des modèles de ML.

- **Optimisation des Modèles** : Explorer d'autres algorithmes de machine learning ou de deep learning, tels que les random forest ou les RNN, pour améliorer les performances des prédictions. 

- **Scalabilité et Performance** : Améliorer la scalabilité du pipeline de données en optimisant l'utilisation de Spark et en explorant des solutions de calcul distribué supplémentaires comme Apache Flink. 

- **Automatisation des Pipelines** : Mettre en place des pipelines de traitement et d'analyse de données automatisés utilisant des technologies comme Airflow ou Kubeflow. en production.

- **Visualisations Améliorées** : Développer des visualisations interactives plus avancées, permettant aux utilisateurs d'explorer dynamiquement les trajectoires et les prédictions de collision des astéroïdes. L'utilisation de technologies comme WebGL pourrait enrichir l'expérience utilisateur.

---

## Conclusion

### Perspectives Futures

- **Travail Futur** : 
	•	Amélioration des Modèles : Explorer des modèles avancés, comme les réseaux de neurones profonds, pour améliorer les prédictions de collision.
	•	Intégration de Données Réelles : Utiliser des données astronomiques réelles pour affiner les simulations et accroître le réalisme des résultats.
	•	Optimisation des Performances : Optimiser le traitement des données avec Spark et envisager d’autres solutions comme Apache Flink pour améliorer l’efficacité.
	•	Visualisations Interactives : Améliorer les visualisations interactives pour permettre une exploration plus intuitive des trajectoires et des risques.

---

## Annexes

### Code Source

![Utilisation de volumes](images/SparkMasterVolumes.png)
![Génération des asteroïdes](images/CodeGenerationAsteroides.png)

### Données

- **Exemples** : Voici des exemples de données utilisées pour les tests et l’entraînement, représentant des astéroïdes avec leurs positions, vitesses, tailles, et masses :

```json
[
  {
    "id": "asteroid_000",
    "position": {
      "x": 222699.68154550303,
      "y": -170502.49676500133,
      "z": 96286.63452916636
    },
    "velocity": {
      "vx": -44.97868922069429,
      "vy": -43.36883583999207,
      "vz": -25.59081952536193
    },
    "size": 7.4,
    "mass": 326766029087404.1
  },
  {
    "id": "asteroid_001",
    "position": {
      "x": 241510.24486868948,
      "y": -168452.54814790297,
      "z": -69360.43184168254
    },
    "velocity": {
      "vx": 26.831251068521794,
      "vy": -1.8149620055246487,
      "vz": -46.032363223946696
    },
    "size": 9.44,
    "mass": 870778504940109.8
  },
  {
    "id": "asteroid_002",
    "position": {
      "x": 388430.33475928206,
      "y": 103642.09747688752,
      "z": 77811.35800764093
    },
    "velocity": {
      "vx": 25.627763490355875,
      "vy": -10.60880719214665,
      "vz": -17.034735038669922
    },
    "size": 6.05,
    "mass": 594347471261444.2
  },
  {
    "id": "asteroid_003",
    "position": {
      "x": 408252.9731877086,
      "y": 171151.49242054566,
      "z": 34378.74584184485
    },
    "velocity": {
      "vx": 18.25062679578167,
      "vy": -18.976092532415546,
      "vz": -30.3861330406611
    },
    "size": 2.74,
    "mass": 350618904146509.5
  }
]

## Équipe

Ce projet a été réalisé par :

- Arnaud LAGARDE ([GitHub](https://github.com/arnaudlagarde))
- Pierre-Antoine SAMUEL ([GitHub](https://github.com/PAS2024))
- Nadim HAMIMID ([GitHub](https://github.com/NadimHipssi))