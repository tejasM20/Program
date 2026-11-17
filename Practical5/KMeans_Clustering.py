# Practical 5: K-Means Clustering
# Dataset: sales_data_sample.csv

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.cluster import KMeans

# Step 2: Load the dataset
dataset_path = Path(__file__).resolve().parent / "dataset" / "sales_data_sample.csv"

df = pd.read_csv(dataset_path, encoding="latin1")

print("First 5 rows of dataset:")
print(df.head())

# Step 3: Select input features
X = df[["QUANTITYORDERED", "PRICEEACH"]]

# Step 4: Apply Elbow Method
sse = []

print("\nSSE Values:")

for k in range(1, 6):

    model = KMeans(n_clusters=k, random_state=42, n_init=10)

    model.fit(X)

    sse.append(model.inertia_)

    print("K =", k, "SSE =", round(model.inertia_, 2))

# Step 5: Plot Elbow Method graph
plt.figure(figsize=(7, 5))

plt.plot(range(1, 6), sse, marker="o")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("SSE")
plt.title("Elbow Method")
plt.xticks(range(1, 6))
plt.grid(True)

plt.show()

# Step 6: Create final K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Step 7: Predict clusters
df["Cluster"] = model.fit_predict(X)

# Step 8: Display cluster results
print("\nCluster Results:")

print(df[["QUANTITYORDERED", "PRICEEACH", "Cluster"]].head())

# Step 9: Visualize the clusters
plt.figure(figsize=(8, 5))

plt.scatter(df["QUANTITYORDERED"], df["PRICEEACH"], c=df["Cluster"], cmap="viridis")

plt.xlabel("Quantity Ordered")
plt.ylabel("Price Each")
plt.title("K-Means Sales Clustering")

plt.show()

print("\nK-Means Clustering Completed!")
