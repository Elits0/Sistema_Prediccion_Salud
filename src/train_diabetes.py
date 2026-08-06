# ==========================================
# SISTEMA DE PREDICCIÓN DE DIABETES
# Entrenamiento del modelo
# ==========================================

import os
import joblib
import warnings
from preprocess import preparar_datos
from utils import evaluar

warnings.filterwarnings("ignore")

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

from sklearn.ensemble import GradientBoostingClassifier

from imblearn.over_sampling import SMOTE

print("="*60)
print("CARGANDO DATASET...")
print("="*60)

from config import DIABETES_DATA

df = pd.read_csv(DIABETES_DATA)

print("\nDataset cargado correctamente.")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())

X_train, X_test, y_train, y_test = preparar_datos(
    df,
    "Diabetes_binary"
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

from config import DIABETES_MODEL

joblib.dump(
    list(X_train.columns),
    "models/columnas_diabetes.pkl"
)

print("\nModelo guardado correctamente.")