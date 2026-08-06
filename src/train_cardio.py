import warnings
warnings.filterwarnings("ignore")

import os
import joblib
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier

from preprocess import preparar_datos
from utils import evaluar

print("="*60)
print("MODELO CARDIOVASCULAR")
print("="*60)

df = pd.read_csv("data/cardio_limpio.csv")

print(df.head())

# Crear BMI
df["BMI"] = df["weight"] / ((df["height"]/100)**2)

X_train, X_test, y_train, y_test = preparar_datos(
    df,
    "cardio"
)

print("\nPreprocesamiento completado.")

print("\nEntrenando modelo...")

modelo = GradientBoostingClassifier(
    random_state=42
)

modelo.fit(
    X_train,
    y_train
)

print("Modelo entrenado correctamente.")

evaluar(modelo, X_test, y_test)

os.makedirs("models", exist_ok=True)

joblib.dump(
    list(X_train.columns),
    "models/columnas_cardio.pkl"
)

print("\nModelo cardiovascular guardado correctamente.")