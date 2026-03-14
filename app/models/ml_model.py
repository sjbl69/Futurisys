import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier


MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../data/model.joblib")


def load_model():

    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    # modèle de secours pour les tests CI
    model = RandomForestClassifier()

    X = [
        [1,2,3,4],
        [4,3,2,1],
        [1,1,1,1],
        [4,4,4,4]
    ]

    y = [0,1,0,1]

    model.fit(X, y)

    return model


model = load_model()


def predict(features):

    X = np.array(features).reshape(1, -1)

    prediction = model.predict(X)

    return float(prediction[0])