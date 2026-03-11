# Futurisys ML API

Futurisys est une API développée avec **FastAPI** permettant de déployer un modèle de **Machine Learning** en production.  
Le projet expose un modèle de classification via une API REST documentée automatiquement avec **Swagger/OpenAPI**.

Futurisys/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── database/
│
├── ml_model/
│   ├── train_model.py
│   └── model.pkl
│
├── tests/
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

Table : predictions

| Column | Type | Description |
|------|------|------|
| id | Integer | Primary key |
| feature1 | Float | Input feature |
| feature2 | Float | Input feature |
| prediction | Float | Model prediction |
| created_at | DateTime | Timestamp |

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

## Database schema

Table: predictions

| Column      | Type      | Description |
|-------------|-----------|-------------|
| id          | Integer   | Primary key |
| feature1    | Float     | Input feature |
| feature2    | Float     | Input feature |
| prediction  | Float     | Model prediction |
| created_at  | DateTime  | Timestamp of prediction |

# Technologies utilisées

- Python
- FastAPI
- Scikit-learn
- Pytest
- GitHub Actions
- Hugging Face Spaces

---

# Auteur

Projet réalisé dans le cadre d’un projet de déploiement de modèle de machine learning.
 
 
 



