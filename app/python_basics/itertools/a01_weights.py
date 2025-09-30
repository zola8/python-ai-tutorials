from itertools import combinations


def calculate_liftable_weights(weights, max_capacity):
    """
    Calculate all possible combinations of weights that can be lifted
    without exceeding the maximum capacity.

    Args:
        weights (list): List of individual weights
        max_capacity (int/float): Maximum weight capacity

    Returns:
        dict: Dictionary containing:
            - 'combinations': list of tuples representing valid combinations
            - 'total_weights': list of total weights for each combination
            - 'max_achievable': maximum weight that can be achieved
    """
    valid_combinations = []
    total_weights = []

    # Check all possible combinations (including empty set)
    for r in range(len(weights) + 1):
        for combo in combinations(weights, r):
            total = sum(combo)
            if 0 < total <= max_capacity:       # exclude empty
                valid_combinations.append(combo)
                total_weights.append(total)

    # Find the maximum achievable weight
    max_achievable = max(total_weights) if total_weights else 0

    return {
        'combinations': valid_combinations,
        'total_weights': total_weights,
        'max_achievable': max_achievable
    }


if __name__ == '__main__':
    # Example usage
    weights = [1, 2, 3]
    max_capacity = 7

    result = calculate_liftable_weights(weights, max_capacity)

    print(f"Weights: {weights}")
    print(f"Max capacity: {max_capacity}")
    print(f"\nAll possible combinations you can lift:")
    for combo, total in zip(result['combinations'], result['total_weights']):
        if combo:  # Skip empty combination if you don't want to show it
            print(f"  {combo} = {total}")

    print(f"\nMaximum weight you can achieve: {result['max_achievable']}")
