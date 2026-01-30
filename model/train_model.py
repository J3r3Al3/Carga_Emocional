import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os
import nltk
from nltk.corpus import stopwords

def train_sentiment_model(max_features=5000, max_iter=200, language='es'):
    try:
        nltk.download('stopwords', quiet=True)
        data = pd.read_csv("data/imdb_reviews.csv")
        
        # 1. Filtrar por idioma
        df = data[data['language'] == language]
        
        if df.empty:
            return {"error": f"No hay datos para el idioma: {language}"}

        # 2. Configurar stop words
        stop_p = 'english' if language == 'en' else list(stopwords.words('spanish'))
        
        # 3. Dividir los datos ANTES de vectorizar (lo correcto en ML)
        X_train, X_test, y_train, y_test = train_test_split(
            df["review"], df["sentiment"], test_size=0.2, random_state=42
        )

        # 4. Vectorización
        # Cambia el vectorizador para que sea más inteligente
        vectorizer = TfidfVectorizer(stop_words=stop_p, max_features=max_features, ngram_range=(1,2))
        X_train_vec = vectorizer.fit_transform(X_train) # Aquí se define la variable
        X_test_vec = vectorizer.transform(X_test)
        
        # 5. Entrenamiento Real
        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train_vec, y_train)

        # 6. Cálculo de precisión real
        y_pred = model.predict(X_test_vec)
        acc_real = accuracy_score(y_test, y_pred)
        
        # 7. Guardar archivos con sufijos correctos
        os.makedirs("model", exist_ok=True)
        sufijo = "_en" if language == 'en' else ""
        joblib.dump(model, f"model/sentiment_model{sufijo}.pkl")
        joblib.dump(vectorizer, f"model/vectorizer{sufijo}.pkl")
        
        # Retornar el valor real (Adiós al Modo Demo)
        return {"accuracy": f"{acc_real:.2%}"}
        
    except Exception as e:
        return {"error": str(e)}