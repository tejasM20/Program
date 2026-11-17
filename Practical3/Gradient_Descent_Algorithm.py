# Practical 3: Gradient Descent Algorithm
# Find the local minimum of y = (x + 3)^2

# Step 1: Initialize the starting point
x = 2

# Step 2: Set the learning rate
lr = 0.1

# Step 3: Perform 20 iterations
for i in range(20):

    # Calculate the gradient
    gradient = 2 * (x + 3)

    # Update x using Gradient Descent
    x = x - lr * gradient

# Step 4: Calculate the minimum y value
y = (x + 3) ** 2

# Step 5: Display the result
print("Minimum x =", round(x, 4))
print("Minimum y =", round(y, 4))
