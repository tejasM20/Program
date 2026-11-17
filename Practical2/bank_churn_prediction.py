import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense

df = pd.read_csv(r"D:\Practicals\ML\Practical2\dataset\Churn_Modelling.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()


# Step 3: Data preprocessing

# Remove unnecessary columns
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Convert Gender into numerical values
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

# Convert Geography into numerical columns
df = pd.get_dummies(df, columns=["Geography"], drop_first=True, dtype=int)

# Separate input and output variables
X = df.drop("Exited", axis=1)
y = df["Exited"]


# Step 4: Split dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# Step 5: Feature scaling

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Step 6: Build Artificial Neural Network

model = Sequential()

# Input layer
model.add(Input(shape=(X_train.shape[1],)))

# First hidden layer
model.add(Dense(16, activation="relu"))

# Second hidden layer
model.add(Dense(8, activation="relu"))

# Output layer
model.add(Dense(1, activation="sigmoid"))


# Step 7: Compile the ANN model

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])


# Step 8: Train the model

history = model.fit(
    X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1
)


# Step 9: Make predictions

y_pred = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (y_pred > 0.5).astype(int).flatten()


# Step 10: Evaluate the model

print("\nModel Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


# Step 11: Display Confusion Matrix

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Not Exited", "Exited"],
    yticklabels=["Not Exited", "Exited"],
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Bank Customer Churn Prediction")
plt.show()


# Step 12: Display Training Accuracy

plt.figure(figsize=(7, 4))

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("ANN Model Accuracy")
plt.legend()
plt.show()


print("\nBank Customer Churn Prediction Completed!")
