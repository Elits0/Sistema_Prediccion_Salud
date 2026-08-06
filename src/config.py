import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

DIABETES_DATA = os.path.join(
    DATA_DIR,
    "diabetes_binary_health_indicators_BRFSS2015.csv"
)

CARDIO_DATA = os.path.join(
    DATA_DIR,
    "cardio_train.csv"
)

DIABETES_MODEL = os.path.join(
    MODELS_DIR,
    "modelo_diabetes.pkl"
)

CARDIO_MODEL = os.path.join(
    MODELS_DIR,
    "modelo_cardio.pkl"
)

