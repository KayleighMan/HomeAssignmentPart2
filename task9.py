import random
import math

def run_simulation(n):
    results = []

    for _ in range(n):
        c1 = random.randint(0, 1)
        c2 = random.randint(0, 1)

        if c1 == 1 or c2 == 1:  # At least one girl
            results.append(1 if (c1 == 1 and c2 == 1) else 0)

    mean = sum(results) / len(results)
    variance = sum((x - mean) ** 2 for x in results) / (len(results) - 1)
    std_dev = math.sqrt(variance)

    return mean, std_dev, len(results)

def calculate_confidence_interval(mean, std_dev, n):
    margin = 2.58 * (std_dev / math.sqrt(n))
    lower = mean - margin
    upper = mean + margin
    return lower, upper

# Sample sizes
sample_sizes = [10000, 20000, 100000]

for size in sample_sizes:
    mean, std_dev, filtered_n = run_simulation(size)
    ci_low, ci_high = calculate_confidence_interval(mean, std_dev, filtered_n)
    print(f"\nSample size: {size}")
    print(f"Filtered (at least one girl): {filtered_n}")
    print(f"Estimated probability: {mean:.4f}")
    print(f"Standard deviation: {std_dev:.6f}")
    print(f"99% Confidence Interval: [{ci_low:.4f}, {ci_high:.4f}]")
