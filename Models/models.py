from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from xgboost import XGBClassifier


def obtener_modelos():

    modelos = {

        "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=42
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=300,
                random_state=42
            ),

        "XGBoost":
            XGBClassifier(
                random_state=42,
                eval_metric="logloss"
            )
    }

    return modelos