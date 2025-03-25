import random

def simulate_two_girls_fallacy(sample_size=10000):
    families_with_at_least_one_girl = 0
    families_with_two_girls = 0

    for _ in range(sample_size):
        # 0 = boy, 1 = girl
        child1 = random.randint(0, 1)
        child2 = random.randint(0, 1)

        if child1 == 1 or child2 == 1:  # At least one girl
            families_with_at_least_one_girl += 1

            if child1 == 1 and child2 == 1:  # Both are girls
                families_with_two_girls += 1

    estimated_probability = families_with_two_girls / families_with_at_least_one_girl

    print(f"Sample Size: {sample_size}")
    print(f"Families with at least one girl: {families_with_at_least_one_girl}")
    print(f"Families with two girls: {families_with_two_girls}")
    print(f"Estimated Probability that the other child is also a girl: {estimated_probability:.4f}")

simulate_two_girls_fallacy()
