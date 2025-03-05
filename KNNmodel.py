
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, request, jsonify
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier

dataset = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)

k=3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
joblib.dump(model, "KNeighbors.pkl")
model = joblib.load("KNeighbors.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        prediction = accuracy_score(y_test, y_pred)        
        return jsonify({"model": "KNeighbors", "prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5001, debug=True)