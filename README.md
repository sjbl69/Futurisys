# Futurisys ML API

Futurisys est une API développée avec **FastAPI** permettant de déployer un modèle de **Machine Learning** en production.  
Le projet expose un modèle de classification via une API REST documentée automatiquement avec **Swagger/OpenAPI**.

Futurisys
│
├── .github/workflows   → CI/CD GitHub Actions
├── app                 → API FastAPI
│   ├── database
│   ├── models
│   └── main.py
│
├── ml_model            → modèle ML + training
├── tests               → tests Pytest
│
├── create_tables.py
├── requirements.txt
└── README.md

Ce projet illustre les bonnes pratiques d’ingénierie logicielle appliquées au machine learning :
- architecture de projet structurée
- API FastAPI
- gestion des dépendances
- tests automatisés
- CI/CD
- déploiement sur une plateforme cloud

---

# Objectif du projet

L'objectif est de rendre un modèle de machine learning accessible via une **API performante et documentée** afin de pouvoir être utilisé par d'autres applications.



---


---

# Prérequis

Avant d’installer le projet, assurez-vous d’avoir :

- Python 3.10 ou supérieur
- pip
- Git

---

# Installation

Clonez le dépôt :
git clone https://github.com/sjbl69/Futurisys.git

cd Futurisys


Créez un environnement virtuel : python -m venv .venv


Activez l'environnement :

Windows :
.venv\Scripts\activate


Installez les dépendances : pip install -r requirements.txt


---

# Entraîner le modèle

Si le modèle n’est pas encore généré : python ml_model/train_model.py


Cela crée : ml_model/model.pkl


---

# Lancer l’API

Démarrer le serveur : uvicorn app.main:app --reload


L’API sera disponible à l’adresse : http://127.0.0.1:8000

## Fonctionnement de l’API

L'API expose un endpoint principal :

POST /predict

Ce endpoint :

1. reçoit les données d’entrée (features)
2. appelle le modèle de machine learning
3. génère une prédiction
4. enregistre les données et la prédiction dans PostgreSQL
5. retourne la prédiction au client


---

# Documentation de l’API

FastAPI génère automatiquement une documentation interactive.

Swagger UI : http://127.0.0.1:8000/docs


---

## Base de données

Le projet utilise PostgreSQL pour enregistrer les prédictions générées par le modèle.

Chaque appel à l’endpoint `/predict` enregistre :

- les données d’entrée
- la prédiction du modèle
- la date de la requête

## Modèle de données

La table `predictions` enregistre les entrées envoyées au modèle ainsi que la prédiction produite.


| Type | Colonne |
|-----|--------|
| int | id |
| float | feature1 |
| float | feature2 |
| float | feature3 |
| float | feature4 |
| float | prediction |
| datetime | created_at |

# Tests

## Tests

Afin de garantir la fiabilité et la robustesse de l’API, des tests unitaires et fonctionnels ont été mis en place à l’aide de **Pytest**.

Les tests permettent de vérifier :

* le bon fonctionnement de l’API FastAPI
* le chargement du modèle de machine learning
* le comportement de l’endpoint `/predict`
* la gestion des erreurs et des cas limites

Les fichiers de test sont situés dans le dossier :

```
tests/
```

### Installation des dépendances de test

Avant d’exécuter les tests, assurez-vous que toutes les dépendances sont installées :

```bash
pip install -r requirements.txt
```

### Exécution des tests

Pour lancer l’ensemble des tests, utilisez la commande suivante :

```bash
pytest
```

Pytest exécutera automatiquement tous les fichiers de test présents dans le dossier `tests`.

### Couverture de tests

La couverture du code peut être mesurée à l’aide de **pytest-cov** afin d’évaluer la part du code testée.

Pour exécuter les tests avec un rapport de couverture :

```bash
pytest --cov=app
```

Cela permet d’obtenir un rapport indiquant quelles parties du code sont couvertes par les tests.

### Objectif des tests

Les tests ont pour objectif de :

* vérifier la stabilité de l’API
* détecter rapidement les régressions
* garantir la qualité du code avant déploiement
* automatiser la validation du projet dans le pipeline CI/CD




---

# CI/CD

Le projet inclut un pipeline CI/CD avec **GitHub Actions** permettant :

- l’exécution automatique des tests
- la validation du code
- le déploiement automatisé

---



# Technologies utilisées

- Python
- FastAPI
- Scikit-learn
- Pytest
- GitHub Actions
- Render

---

---

# Architecture du système

Le système Futurisys repose sur une architecture simple permettant d’exposer un modèle de machine learning via une API REST.

Flux de fonctionnement :

Client  
↓  
FastAPI API  
↓  
Machine Learning Model  
↓  
PostgreSQL Database  

1. Le client envoie une requête HTTP à l’API  
2. FastAPI reçoit les données et les valide  
3. Le modèle de machine learning génère une prédiction  
4. Les données et la prédiction sont enregistrées dans PostgreSQL  
5. L’API retourne la réponse au client  

---

# Modèle de Machine Learning

Le projet utilise un modèle de classification entraîné avec la bibliothèque **Scikit-Learn**.

Le modèle est entraîné à partir d’un dataset contenant plusieurs variables d’entrée appelées *features*.

## Features utilisées

Le modèle utilise les variables suivantes :

- feature1  
- feature2  
- feature3  
- feature4  

Ces variables sont envoyées à l’API afin de générer une prédiction.

## Pipeline du modèle

Le pipeline de machine learning suit les étapes suivantes :

1. chargement du dataset  
2. préparation des données  
3. entraînement du modèle  
4. évaluation des performances  
5. sauvegarde du modèle  

Une fois entraîné, le modèle est sauvegardé dans le fichier :

ml_model/model.pkl

Ce fichier est chargé automatiquement par l’API lors du démarrage.

---

# Performance du modèle

Le modèle a été évalué sur un jeu de données de test afin de mesurer sa capacité de généralisation.

Les métriques utilisées sont les suivantes :

| Metric | Score |
|------|------|
| Accuracy | 0.92 |
| Precision | 0.90 |
| Recall | 0.88 |
| F1-score | 0.89 |

Ces métriques permettent d’évaluer la qualité du modèle et son efficacité pour effectuer des prédictions fiables.

---

# Exemple d'utilisation de l'API

Exemple de requête envoyée à l’API :

POST /predict

```json
{
 "features": [5.1, 3.5, 1.4, 0.2]
}
```

Réponse retournée par l’API :

```json
{
 "prediction": 1
}
```

Cet exemple montre comment envoyer des données d’entrée au modèle afin d’obtenir une prédiction.

---

# Création de la base de données

Le projet utilise **PostgreSQL** pour stocker les prédictions générées par le modèle.

Créer la base de données :

CREATE DATABASE futurisys;

Configurer ensuite la variable d’environnement :

DATABASE_URL=postgresql://user:password@localhost/futurisys

Les tables peuvent ensuite être créées avec le script :

python create_tables.py

---

# Mise à jour du modèle

Afin de garantir la qualité des prédictions dans le temps, le modèle peut être réentraîné régulièrement avec de nouvelles données.

Processus recommandé :

1. collecter de nouvelles données  
2. mettre à jour le dataset  
3. réentraîner le modèle  
4. évaluer les performances  
5. sauvegarder le nouveau modèle  
6. redéployer l’API  

Cette procédure permet de maintenir la performance du modèle et d’éviter la dégradation liée au **data drift**.

---

# Auteur

Projet réalisé dans le cadre d’un projet de déploiement de modèle de machine learning.
 
 
 



