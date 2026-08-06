from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def preparar_datos(df, target):

    X = df.drop(target, axis=1)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    smote = SMOTE(random_state=42)

    X_train, y_train = smote.fit_resample(
        X_train,
        y_train
    )

    return X_train, X_test, y_train, y_test