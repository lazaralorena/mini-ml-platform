"""Script to train and export a Random Forest classifier using the Iris dataset."""

import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Ensure the directory exists for saving the model
os.makedirs("serve", exist_ok=True)

# Load Iris dataset
iris_data = load_iris()
X = iris_data.data  # pylint: disable=no-member
y = iris_data.target  # pylint: disable=no-member

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "serve/model.pkl")
print("Model trained and saved to serve/model.pkl")
