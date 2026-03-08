# Futurisys ML API

Futurisys est une API développée avec **FastAPI** permettant de déployer un modèle de **Machine Learning** en production.  
Le projet expose un modèle de classification via une API REST documentée automatiquement avec **Swagger/OpenAPI**.

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

Le modèle est entraîné sur le dataset **Iris** et permet de prédire la classe d'une fleur à partir de ses caractéristiques.

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


---

# Documentation de l’API

FastAPI génère automatiquement une documentation interactive.

Swagger UI : http://127.0.0.1:8000/docs


---

# Tests

Les tests peuvent être exécutés avec **Pytest** :



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
- Hugging Face Spaces

---

# Auteur

Projet réalisé dans le cadre d’un projet de déploiement de modèle de machine learning.
 
 
 



