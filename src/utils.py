from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


def evaluar(modelo, X_test, y_test):

    pred = modelo.predict(X_test)

    prob = modelo.predict_proba(X_test)[:,1]

    print("\nAccuracy :", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall   :", recall_score(y_test, pred))
    print("F1       :", f1_score(y_test, pred))
    print("ROC AUC  :", roc_auc_score(y_test, prob))
    evaluar(modelo, X_test, y_test)
    