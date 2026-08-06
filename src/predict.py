import joblib
import pandas as pd

# ==========================
# Cargar modelos
# ==========================

modelo_diabetes = joblib.load("Models/modelo_diabetes.pkl")
modelo_cardio = joblib.load("Models/modelo_cardio.pkl")

columnas_diabetes = joblib.load("Models/columnas_diabetes.pkl")
columnas_cardio = joblib.load("Models/columnas_cardio.pkl")


def predecir_diabetes(datos):

    df = pd.DataFrame([datos])

    # Orden correcto de columnas
    df = df[columnas_diabetes]

    probabilidad = modelo_diabetes.predict_proba(df)[0][1]
    prediccion = modelo_diabetes.predict(df)[0]

    return prediccion, probabilidad


def predecir_cardio(datos):

    df = pd.DataFrame([datos])

    # Orden correcto de columnas
    df = df[columnas_cardio]

    probabilidad = modelo_cardio.predict_proba(df)[0][1]
    prediccion = modelo_cardio.predict(df)[0]

    return prediccion, probabilidad