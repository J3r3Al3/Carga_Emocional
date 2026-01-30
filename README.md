## Analizador de Sentimiento - FIA EPN

Sistema integral de análisis de sentimientos bilingüe desarrollado para el Proyecto Final de Inteligencia Artificial. La aplicación utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) para clasificar opiniones como **Positivas** o **Negativas**.

---

## Descripción del Proyecto
Este software implementa un modelo de **Regresión Logística** entrenado con un corpus global balanceado. El sistema está diseñado bajo una arquitectura de microservicios, separando la interfaz de usuario (Cliente) del motor de inferencia (Servidor API).

### Características Principales:
* **Soporte Bilingüe:** Procesamiento independiente para Español (ES) e Inglés (EN).
* **Preprocesamiento Avanzado:** Uso de TF-IDF Vectorization con N-gramas (1,2).
* **Entrenamiento en Caliente:** Capacidad de re-entrenar el modelo desde la interfaz gráfica.
* **Visualización de Métricas:** Muestra el Accuracy real obtenido tras cada entrenamiento.

---

## Requisitos del Sistema
Es necesario contar con Python 3.10 o superior y las siguientes dependencias:

```bash
pip install flask pandas scikit-learn nltk joblib requests
```
## Estructura de Archivos

```bash
sentiment_ai_project/
│
├── api/
│   └── app.py              # Servidor Flask (API REST)
├── gui/
│   └── app.py              # Interfaz Gráfica (Tkinter)
├── model/
│   ├── train_model.py      # Lógica de ML y Entrenamiento
│   └── *.pkl               # Modelos y vectorizadores guardados
├── data/
│   └── imdb_reviews.csv    # Dataset global (60 registros)
└── README.md               # Documentación del proyecto
```

## GUÍA DE EJECUCIÓN TÉCNICA
1. Requisitos Previos e Instalación
Antes de iniciar, asegúrese de tener instaladas todas las dependencias necesarias ejecutando el siguiente comando en su terminal:

```bash
pip install flask pandas scikit-learn nltk joblib requests
```
2. Preparación del Entorno
Es fundamental ejecutar el main en la terminal de VS Code para hacer funcionar el programa

```bash
python main.py
```

3. Operación del Sistema (Flujo de Trabajo)
Para garantizar que el modelo utilice la información más reciente del dataset, siga este flujo:
* **Selección de Idioma:** Elija entre Español o English en los botones de selección.
* **Sincronización (Entrenamiento):** Presione el botón ENTRENAR.
* **Nota:** El sistema procesará el dataset y mostrará el Accuracy real (75% - 76%). Este paso genera los archivos .pkl necesarios.
* **Análisis de Texto:**
Escriba una opinión en el cuadro de texto (ej: "El servicio fue excelente").
Presione el botón ANALIZAR.
El sistema consultará a la API y mostrará el veredicto (POSITIVO/NEGATIVO) con un color indicativo.

## Demostración en Video
Puedes ver el funcionamiento del proyecto en el siguiente enlace:
[Ver video de demostración aquí](https://youtu.be/jrLu7xhFWfI)
