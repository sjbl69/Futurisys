import joblib
import os
import numpy as np

# chemin vers le modèle sauvegardé
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../data/model.joblib")

# chargement du modèle au démarrage
model = joblib.load(MODEL_PATH)


def predict(features):
    """
    Prend une liste de 4 features et retourne une prédiction du modèle.
    """

    # convertir en array numpy 2D (format attendu par sklearn)
    X = np.array(features).reshape(1, -1)

    prediction = model.predict(X)

    # retourner un float simple
    return float(prediction[0])