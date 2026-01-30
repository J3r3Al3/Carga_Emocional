import tkinter as tk
from tkinter import messagebox
import requests
import os
import sys

# Ajuste de rutas para importar la función de entrenamiento desde la raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.train_model import train_sentiment_model

API_URL = "http://127.0.0.1:5000/predict"

def run_training():
    try:
        m_features = int(features_entry.get())
        m_iter = int(iter_entry.get())
        idioma = lang_var.get()
        
        root.config(cursor="watch")
        root.update()
        
        # Llamada a la función de entrenamiento con el parámetro de idioma
        res = train_sentiment_model(max_features=m_features, max_iter=m_iter, language=idioma)
        
        if "error" in res:
            messagebox.showerror("Error", res["error"])
        else:
            accuracy_val.config(text=f"Accuracy ({idioma.upper()}): {res['accuracy']}", fg="#2ecc71")
            messagebox.showinfo("Éxito", f"Modelo {idioma.upper()} entrenado con {res['accuracy']}")
        
        root.config(cursor="")
    except Exception as e:
        root.config(cursor="")
        messagebox.showerror("Error", f"Error en entrenamiento: {e}")

def analyze_sentiment():
    review = entry.get("1.0", tk.END).strip()
    idioma = lang_var.get()
    
    if not review: return

    try:
        # Enviamos idioma y texto a la API
        response = requests.post(API_URL, json={"review": review, "language": idioma})
        
        if response.status_code == 200:
            sentiment = response.json()["sentiment"]
            color = "green" if sentiment == "positivo" else "red"
            result_label.config(text=f"SENTIMIENTO ({idioma.upper()}): {sentiment.upper()}", fg=color)
        else:
            messagebox.showwarning("Aviso", "Entrena el modelo primero para este idioma")
    except Exception as e:
        messagebox.showerror("Error", f"La API no responde: {e}")

# --- Configuración Visual de Tkinter ---
root = tk.Tk()
root.title("Bilingual Sentiment Analyzer - EPN")
root.geometry("500x650")
root.configure(bg="#f0f0f0")

# Selector de Idioma
lang_frame = tk.LabelFrame(root, text=" Idioma / Language ", padx=10, pady=5)
lang_frame.pack(pady=10, padx=20, fill="x")

lang_var = tk.StringVar(value="es")
tk.Radiobutton(lang_frame, text="Español 🇪🇸", variable=lang_var, value="es").pack(side=tk.LEFT, padx=20)
tk.Radiobutton(lang_frame, text="English 🇺🇸", variable=lang_var, value="en").pack(side=tk.LEFT, padx=20)

# Sección Entrenamiento
train_frame = tk.LabelFrame(root, text=" Configuración y Entrenamiento ", padx=10, pady=10)
train_frame.pack(pady=10, padx=20, fill="x")

tk.Label(train_frame, text="Max Features:").grid(row=0, column=0)
features_entry = tk.Entry(train_frame, width=10); features_entry.insert(0, "5000"); features_entry.grid(row=0, column=1)

tk.Label(train_frame, text="Iteraciones:").grid(row=1, column=0)
iter_entry = tk.Entry(train_frame, width=10); iter_entry.insert(0, "200"); iter_entry.grid(row=1, column=1)

tk.Button(train_frame, text="ENTRENAR", command=run_training, bg="#3498db", fg="white").grid(row=0, column=2, rowspan=2, padx=10)
accuracy_val = tk.Label(train_frame, text="Accuracy: --%", font=("bold", 10))
accuracy_val.grid(row=2, column=0, columnspan=3, pady=5)

# Sección Análisis
tk.Label(root, text="Escribe tu reseña / Write your review:", bg="#f0f0f0").pack(pady=5)
entry = tk.Text(root, height=5, font=("Helvetica", 11)); entry.pack(padx=20, pady=10)

tk.Button(root, text="ANALIZAR", command=analyze_sentiment, bg="#2ecc71", fg="white", font=("bold", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("bold", 16), bg="#f0f0f0")
result_label.pack(pady=20)

# El comando mainloop es lo que mantiene la ventana abierta
root.mainloop()