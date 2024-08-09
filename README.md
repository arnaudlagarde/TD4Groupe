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
  - [Références](#références)
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


## Stockage et Traitement des Données

### Stockage dans Hadoop (HDFS)

- **Consommateur Kafka** : Configurez un consommateur Kafka pour lire les données des astéroïdes et les stocker dans HDFS.

### Traitement avec Spark

- **Lecture des Données** : Utilisez Spark pour lire les données stockées dans HDFS.
- **Nettoyage des Données** : Effectuez des opérations de nettoyage et de préparation des données.
- **Analyse des Trajectoires** : Calculez les trajectoires prévues des astéroïdes.

## Modélisation Prédictive

### Sélection des Algorithmes

- **Algorithmes Choisis** : Décrivez les algorithmes que vous avez sélectionnés pour la prédiction. Cela peut inclure des algorithmes de régression logistique, des réseaux de neurones, des machines à vecteurs de support, ou d'autres méthodes de machine learning ou deep learning. Expliquez pourquoi ces algorithmes sont appropriés pour la tâche de prédiction de collision des astéroïdes.

### Entraînement du Modèle

- **Entraînement** : Décrivez le processus d'entraînement du modèle. Cela inclut la préparation des données, le choix des hyperparamètres, et la durée de l'entraînement. Mentionnez les outils et bibliothèques utilisés (comme Scikit-learn, TensorFlow, PyTorch, etc.).

- **Validation** : Présentez les techniques de validation utilisées pour évaluer la performance du modèle. Cela peut inclure la validation croisée, les ensembles de données de validation, et les métriques d'évaluation comme la précision, le rappel, la F-mesure, ou l'AUC-ROC. Discutez des résultats obtenus et de la performance du modèle sur les données de test.

## Visualisation

### Visualisations des Trajectoires

- **Graphiques** : Incluez des graphiques montrant les trajectoires des astéroïdes et les résultats des prédictions. Utilisez des bibliothèques telles que Matplotlib, Seaborn ou Plotly pour créer des visualisations claires et informatives. Ces graphiques peuvent inclure des courbes représentant les trajectoires des astéroïdes dans l'espace, des histogrammes de la taille et de la masse des astéroïdes, ainsi que des graphiques de la probabilité de collision.

## Discussion

### Interprétation des Résultats

- **Analyse** : Discutez des résultats obtenus à partir des modèles et des visualisations.

### Défis Rencontrés

- **Problèmes** : Notez les défis rencontrés durant le projet et comment ils ont été résolus.

### Améliorations

- **Suggestions** : Proposez des améliorations possibles pour les futures itérations du projet.

---

## Conclusion

### Résumé

- **Contributions** : Résumez les principales contributions du projet.

### Perspectives Futures

- **Travail Futur** : Discutez des directions possibles pour le travail futur et des améliorations possibles.

---

## Annexes

### Code Source

- **Scripts** : Incluez des liens ou des extraits de code source utilisé dans le projet.

### Données

- **Exemples** : Fournissez des exemples de données utilisées pour les tests et l’entraînement.

---

## Références

- **Documentation** : Incluez des liens vers la documentation officielle, des articles de recherche, ou d’autres ressources pertinentes.

---

## Équipe

Ce projet a été réalisé par :

- Arnaud LAGARDE ([GitHub](https://github.com/arnaudlagarde))
- Pierre-Antoine SAMUEL ([GitHub](https://github.com/PAS2024))
- Nadim HAMIMID ([GitHub](https://github.com/NadimHipssi))