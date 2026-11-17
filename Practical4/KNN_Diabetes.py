# Practical 4: K-Nearest Neighbors (KNN)
# Diabetes Prediction using diabetes.csv

# Step 1: Import required libraries
import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
)

# Step 2: Load the dataset
dataset_path = Path(__file__).resolve().parent / "dataset" / "diabetes.csv"

df = pd.read_csv(dataset_path)

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# Step 3: Separate input and output variables
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Step 4: Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 5: Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Create KNN model
model = KNeighborsClassifier(n_neighbors=5)

# Step 7: Train the model
model.fit(X_train, y_train)

# Step 8: Predict the results
p = model.predict(X_test)

# Step 9: Calculate confusion matrix
cm = confusion_matrix(y_test, p)

print("\nConfusion Matrix:")
print(cm)

# Step 10: Calculate performance metrics
accuracy = accuracy_score(y_test, p)
error_rate = 1 - accuracy
precision = precision_score(y_test, p, zero_division=0)
recall = recall_score(y_test, p, zero_division=0)

print("\nModel Performance:")
print("Accuracy:", round(accuracy, 3))
print("Error Rate:", round(error_rate, 3))
print("Precision:", round(precision, 3))
print("Recall:", round(recall, 3))

print("\nKNN Diabetes Prediction Completed!")
