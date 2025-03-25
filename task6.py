import random
import math

# --- Step 1: Run simulation with 10,000 samples ---
sample_size = 10000
results = []

for _ in range(sample_size):
    child1 = random.randint(0, 1)
    child2 = random.randint(0, 1)

    if child1 == 1 or child2 == 1:  # At least one girl
        if child1 == 1 and child2 == 1:
            results.append(1)  # Both girls
        else:
            results.append(0)  # Not both girls

# --- Step 2: Calculate sample mean (estimated probability) ---
n = len(results)
mean = sum(results) / n

# --- Step 3: Calculate variance using formula ---
variance = sum((x - mean) ** 2 for x in results) / (n - 1)

# --- Step 4: Calculate RMSE ---
rmse = math.sqrt(variance / n)

# --- Step 5: Calculate new sample size to get RMSE = 0.001 ---
target_rmse = 0.001
new_sample_size = math.ceil(variance / (target_rmse ** 2))

# --- Step 6: Run simulation again with new sample size ---
new_results = []
for _ in range(new_sample_size):
    c1 = random.randint(0, 1)
    c2 = random.randint(0, 1)
    if c1 == 1 or c2 == 1:
        if c1 == 1 and c2 == 1:
            new_results.append(1)
        else:
            new_results.append(0)

new_mean = sum(new_results) / len(new_results)

# --- Output ---
print("Original Sample Size = 10,000")
print("Estimated Probability:", round(mean, 4))
print("Variance:", round(variance, 6))
print("RMSE:", round(rmse, 6))
print("\nNew Sample Size needed for RMSE = 0.001:", new_sample_size)
print("New Estimated Probability:", round(new_mean, 4))
