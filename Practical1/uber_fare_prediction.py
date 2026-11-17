
# Practical 1: Uber Fare Prediction
# Linear Regression and Random Forest Regression

# Step 1: Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# Step 2: Load the dataset

df = pd.read_csv("dataset/uber.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()


# Step 3: Data preprocessing

# Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"], errors="ignore")

# Select required columns
df = df[
    [
        "fare_amount",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "passenger_count"
    ]
]

# Handle missing values
df = df.dropna()

# Remove invalid records
df = df[df["fare_amount"] > 0]
df = df[df["passenger_count"] > 0]

print("\nDataset after preprocessing:")
print(df.head())

print("\nDataset shape:", df.shape)


# Step 4: Outlier detection using IQR

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[
    (df["fare_amount"] >= lower_limit) &
    (df["fare_amount"] <= upper_limit)
]


# Step 5: Correlation heatmap

plt.figure(figsize=(8, 6))

sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.show()


# Step 6: Select input and output variables

X = df[
    [
        "passenger_count",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude"
    ]
]

y = df["fare_amount"]


# Step 7: Split dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 8: Linear Regression

lr = LinearRegression()

lr.fit(X_train, y_train)

p1 = lr.predict(X_test)


# Step 9: Random Forest Regression

rf = RandomForestRegressor(n_estimators=50, random_state=42)

rf.fit(X_train, y_train)

p2 = rf.predict(X_test)


# Step 10: Model evaluation

print("\nLinear Regression Results:")

print("R2 Score:", r2_score(y_test, p1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p1)))


print("\nRandom Forest Regression Results:")

print("R2 Score:", r2_score(y_test, p2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, p2)))


print("\nUber Fare Prediction Completed Successfully!")
