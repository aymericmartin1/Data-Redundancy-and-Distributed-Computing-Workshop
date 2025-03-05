import json
import numpy as np
import joblib
from flask import Flask, request, jsonify
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Charger le dataset
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)

# Entraîner un modèle
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Sauvegarder le modèle
joblib.dump(model, "random_forest_model.pkl")

# Charger le modèle
model = joblib.load("random_forest_model.pkl")

# Initialiser Flask
app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        prediction = accuracy_score(y_test, y_pred)
        
        # Retourner le résultat
        return jsonify({"model": "random_forest", "prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5004, debug=True)
