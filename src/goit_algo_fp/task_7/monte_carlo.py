import random
from collections import Counter

sides = 6
num_dice = 2


def roll_dice() -> int:
    return sum(random.randint(1, sides) for _ in range(num_dice))


def monte_carlo_simulation(num_rolls: int) -> dict[int, float]:
    sums_counter = Counter()

    for _ in range(num_rolls):
        total = roll_dice()
        sums_counter[total] += 1

    probabilities = {
        sum_value: count / num_rolls for sum_value, count in sums_counter.items()
    }

    return probabilities


def get_theoretical_probabilities() -> dict[int, float]:
    theoretical = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }
    return theoretical
