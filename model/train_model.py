import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(
    BASE_DIR,
    "dataset",
    "iris.csv"
)

df = pd.read_csv(dataset_path)


# ============================================================
# 2. SELECT FEATURES
# ============================================================

features = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

X = df[features]


# ============================================================
# 3. SELECT TARGET
# ============================================================

y = df["species"]


# ============================================================
# 4. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 5. CREATE MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ============================================================
# 6. TRAIN MODEL
# ============================================================

model.fit(X_train, y_train)


# ============================================================
# 7. TEST MODEL
# ============================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


# ============================================================
# 8. SAVE MODEL
# ============================================================

model_path = os.path.join(
    BASE_DIR,
    "model",
    "iris_model.pkl"
)

joblib.dump(model, model_path)


# ============================================================
# 9. DISPLAY RESULTS
# ============================================================

print("=" * 50)
print("IRIS FLOWER ML MODEL")
print("=" * 50)

print(f"Dataset rows      : {len(df)}")
print(f"Training rows     : {len(X_train)}")
print(f"Testing rows      : {len(X_test)}")
print(f"Features          : {features}")

print("\nSpecies:")
print(y.unique())

print("\nModel:")
print("Random Forest Classifier")

print(f"\nAccuracy          : {accuracy * 100:.2f}%")

print("\nModel saved successfully!")
print(f"Location          : {model_path}")

print("=" * 50)
