import pandas as pd
import os
import joblib
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords

# 1. Descargas necesarias
print("📥 Descargando herramientas de lenguaje...")
nltk.download('stopwords')

# 2. Crear Dataset balanceado (20 ejemplos claros)
print("📊 Generando dataset balanceado...")
data = {
    review,sentiment
"La pelicula es excelente y muy buena",positivo
"Me gusto mucho la actuacion y el guion",positivo
"Es una obra maestra del cine",positivo
"Fue una experiencia increible y emocionante",positivo
"Realmente recomendada para todos",positivo
"El final fue espectacular y me encanto",positivo
"Una de las mejores peliculas que he visto",positivo
"Todo fue perfecto en esta produccion",positivo
"Es genial ver peliculas de este nivel",positivo
"Me fascino la trama y los personajes",positivo
"La pelicula es malisima y aburrida",negativo
"No me gusto nada, fue una perdida de tiempo",negativo
"Pesima direccion y muy mala historia",negativo
"Es lo peor que he visto en años",negativo
"Me quede dormido de lo lenta que era",negativo
"No la recomiendo para nada, es horrible",negativo
"Un desastre total de principio a fin",negativo
"Actuaciones mediocres y guion sin sentido",negativo
"Muy decepcionado con esta pelicula",negativo
"No gasten su dinero en esta basura",negativo
"Que buena historia tiene esta cinta",positivo
"Los efectos especiales son maravillosos",positivo
"Una pelicula muy entretenida y divertida",positivo
"Simplemente brillante y conmovedora",positivo
"Me encanto cada minuto de la pelicula",positivo
"Es una porqueria no vale la pena",negativo
"Fue un desperdicio total de dinero",negativo
"La peor pelicula de la historia",negativo
"No tiene sentido y es muy larga",negativo
"Odie la pelicula desde el inicio",negativo
}
os.makedirs("data", exist_ok=True)
pd.DataFrame(data).to_csv("data/imdb_reviews.csv", index=False)

# 3. Entrenamiento Limpio (Sin errores de variables)
print("🧠 Entrenando modelo...")
df = pd.read_csv("data/imdb_reviews.csv")
# Definimos las stop words correctamente aquí
lista_stop_words = list(stopwords.words('spanish'))

vectorizer = TfidfVectorizer(stop_words=lista_stop_words, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

model = LogisticRegression()
model.fit(X, y)

# 4. Guardar archivos finales
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ ¡SISTEMA REPARADO! Ahora ejecuta main.py y prueba de nuevo.")