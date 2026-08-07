[1mdiff --git a/src/predict.py b/src/predict.py[m
[1mindex 07f3603..8729eee 100644[m
[1m--- a/src/predict.py[m
[1m+++ b/src/predict.py[m
[36m@@ -5,12 +5,11 @@[m [mimport pandas as pd[m
 # Cargar modelos[m
 # ==========================[m
 [m
[31m-modelo_diabetes = joblib.load("models/modelo_diabetes.pkl")[m
[31m-modelo_cardio = joblib.load("models/modelo_cardio.pkl")[m
[32m+[m[32mmodelo_diabetes = joblib.load("Models/modelo_diabetes.pkl")[m
[32m+[m[32mmodelo_cardio = joblib.load("Models/modelo_cardio.pkl")[m
 [m
[31m-# Cargar columnas[m
[31m-columnas_diabetes = joblib.load("models/columnas_diabetes.pkl")[m
[31m-columnas_cardio = joblib.load("models/columnas_cardio.pkl")[m
[32m+[m[32mcolumnas_diabetes = joblib.load("Models/columnas_diabetes.pkl")[m
[32m+[m[32mcolumnas_cardio = joblib.load("Models/columnas_cardio.pkl")[m
 [m
 [m
 def predecir_diabetes(datos):[m
