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


@app.route('/predict',methods = ['POST'])
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
@app.route('/form')
def form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Titanic Prediction</title>
        <style>
            body { font-family: Arial; padding: 30px; max-width: 600px; margin: auto; }
            input, select { width: 100%; padding: 8px; margin: 8px 0; }
            button { padding: 10px 20px; }
        </style>
    </head>
    <body>
        <h2>Titanic Survival Prediction</h2>
        <form id="predictForm">
            <label>Pclass:</label>
            <select name="Pclass">
                <option value="1">1st</option>
                <option value="2">2nd</option>
                <option value="3" selected>3rd</option>
            </select>

            <label>Sex:</label>
            <select name="Sex">
                <option value="0">Male</option>
                <option value="1">Female</option>
            </select>

            <label>Age:</label>
            <input type="number" name="Age" step="0.1" value="22" required>

            <label>SibSp (siblings/spouses):</label>
            <input type="number" name="SibSp" value="0" required>

            <label>Parch (parents/children):</label>
            <input type="number" name="Parch" value="0" required>

            <label>Fare:</label>
            <input type="number" name="Fare" step="0.01" value="7.25" required>

            <label>Embarked:</label>
            <select name="Embarked">
                <option value="S" selected>Southampton (S)</option>
                <option value="Q">Queenstown (Q)</option>
                <option value="C">Cherbourg (C)</option>
            </select>

            <button type="submit">Predict</button>
        </form>

        <h3 id="result"></h3>

        <script>
        document.getElementById('predictForm').addEventListener('submit', async function(e) {
            e.preventDefault();

            const form = e.target;
            const data = {
                Pclass: parseInt(form.Pclass.value),
                Sex: parseInt(form.Sex.value),
                Age: parseFloat(form.Age.value),
                SibSp: parseInt(form.SibSp.value),
                Parch: parseInt(form.Parch.value),
                Fare: parseFloat(form.Fare.value),
                Embarked_Q: form.Embarked.value === 'Q' ? 1 : 0,
                Embarked_S: form.Embarked.value === 'S' ? 1 : 0
            };

            const response = await fetch('/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });

            const result = await response.json();
            const text = result.prediction === 1 ? '✅ Survived' : '❌ Did Not Survive';
            document.getElementById('result').textContent = "Prediction: " + text;
        });
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')