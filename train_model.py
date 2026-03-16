import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/disease_gene.csv")

# Convert gene names to numeric values
df["gene_encoded"] = df["gene"].astype("category").cat.codes

# Features
X = df[["association_score","gene_encoded"]]

# Target
y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(model,"models/target_model.pkl")

print("Model trained successfully")