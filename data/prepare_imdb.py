import pandas as pd
import os

def prepare_dataset():
    # Creamos un dataset balanceado manualmente para asegurar precisión inicial
    data = {
        "review": [
            "La pelicula estuvo muy buena", "Me encanto el final", "Excelente actuacion",
            "Fue una experiencia increible", "Realmente recomendada", "Muy divertida y emocionante",
            "La pelicula es malisima", "No me gusto nada", "Es muy aburrida",
            "Pesima direccion y guion", "Perdi mi tiempo viendola", "No la recomiendo para nada",
            "El actor principal lo hace genial", "Una obra maestra del cine", "Que buena historia",
            "Todo fue un desastre", "Horrible, no gasten su dinero", "Me quede dormido"
        ],
        "sentiment": [
            "positivo", "positivo", "positivo", "positivo", "positivo", "positivo",
            "negativo", "negativo", "negativo", "negativo", "negativo", "negativo",
            "positivo", "positivo", "positivo", "negativo", "negativo", "negativo"
        ]
    }
    
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/imdb_reviews.csv", index=False, encoding="utf-8")
    print("✅ Dataset en español generado en data/imdb_reviews.csv")

if __name__ == "__main__":
    prepare_dataset()