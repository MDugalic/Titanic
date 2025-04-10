from flask import Flask, request,jsonify
import joblib
import numpy as np

#Inicijalizacija aplikacije

app = Flask(__name__)

model = joblib.load('models/logistic_model.pkl')
#redosled kolona koje tvoj model ocekuje

FEATURE_ORDER = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S']

@app.route('/')
def home():
    return "Titanic Survival Prediction API is runnging!"

@app.route('/predict',methods = ['Post'])
def predict():
    try:
        data = request.get_json()

        input_data = [data.get(col,0) for col in FEATURE_ORDER]
        input_array = np.array(input_data).reshape(1,-1)

        #predikcija
        prediction = model.predict(input_array)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error:':str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)