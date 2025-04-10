# 🧠 Titanic Survival Prediction API

A machine learning project that predicts whether a passenger would survive the Titanic disaster based on their features (class, sex, age, etc). The model is exposed through a Flask API, fully Dockerized and deployed on Render.

---

## 🚀 Live Demo

🌍 Access the live API:  
👉 [https://titanic-u4va.onrender.com](https://titanic-u4va.onrender.com)

---

## 📦 Project Structure


---

## 📈 Features

- Logistic Regression for binary classification
- Cleaned and preprocessed Titanic dataset
- Dockerized for portability
- Deployed on Render (free cloud hosting)
- RESTful API endpoint for prediction

---

## 📬 API Usage

### ➤ Endpoint


### ➤ Example Request (JSON)

```json
{
  "Pclass": 3,
  "Sex": 1,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked_Q": 0,
  "Embarked_S": 1
}
