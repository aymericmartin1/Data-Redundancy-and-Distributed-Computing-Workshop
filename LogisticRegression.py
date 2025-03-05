from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib 
from flask import Flask, request, jsonify



iris=load_breast_cancer()
X=iris.data
y=iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=LogisticRegression()
model.fit(X_train,y_train)

joblib.dump(model, "random_forest_model.pkl")

model = joblib.load("random_forest_model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        accuracy = model.score(X_test, y_test)
        
        return jsonify({"model": "logistic regression", "accuracy": accuracy})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5001, debug=True)