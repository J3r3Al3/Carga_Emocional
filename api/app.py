from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    lang = data.get("language", "es")
    text = data.get("review", "")
    
    # Rutas dinámicas según idioma
    suf = "_en" if lang == 'en' else ""
    m_path = f"model/sentiment_model{suf}.pkl"
    v_path = f"model/vectorizer{suf}.pkl"

    if not os.path.exists(m_path):
        return jsonify({"sentiment": "Error", "message": "Entrena el modelo primero"}), 400

    m = joblib.load(m_path)
    v = joblib.load(v_path)
    pred = m.predict(v.transform([text]))[0]
    return jsonify({"sentiment": pred})

if __name__ == "__main__":
    app.run(port=5000)