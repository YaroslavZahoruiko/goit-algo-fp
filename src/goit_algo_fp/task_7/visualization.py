import matplotlib.pyplot as plt
from typing import Dict


def print_probability_table(
    probabilities: Dict[int, float],
    theoretical: Dict[int, float] | None = None,
    num_rolls: int | None = None,
) -> None:
    print("\n" + "=" * 70)
    print("Probability Table")
    print("=" * 70)
    if num_rolls:
        print(f"Number of rolls: {num_rolls:,}")
    print("-" * 70)
    print(f"{'Sum':<6} {'Probability':<15} {'Percentage':<12}", end="")
    if theoretical:
        print(f"{'Theoretical':<15} {'Difference':<12}")
    else:
        print()
    print("-" * 70)

    all_sums = sorted(
        set(probabilities.keys()) | (set(theoretical.keys()) if theoretical else set())
    )

    for sum_val in all_sums:
        prob = probabilities.get(sum_val, 0.0)
        percentage = prob * 100
        print(f"{sum_val:<6} {prob:<15.6f} {percentage:<12.2f}%", end="")

        if theoretical:
            theo_prob = theoretical.get(sum_val, 0.0)
            theo_percentage = theo_prob * 100
            difference = abs(prob - theo_prob) * 100
            print(f"{theo_percentage:<15.2f}% {difference:<12.4f}%")
        else:
            print()

    print("=" * 70)


def plot_probabilities(
    probabilities: Dict[int, float],
    theoretical: Dict[int, float],
    num_rolls: int | None = None,
) -> None:
    all_sums = sorted(
        set(probabilities.keys()) | (set(theoretical.keys()) if theoretical else set())
    )

    sums = all_sums
    monte_carlo_probs = [probabilities.get(s, 0.0) * 100 for s in sums]
    theoretical_probs = (
        [theoretical.get(s, 0.0) * 100 for s in sums] if theoretical else None
    )

    fig, ax = plt.subplots(figsize=(12, 6))

    x = range(len(sums))
    width = 0.35

    bars1 = ax.bar(
        [i - width / 2 for i in x],
        monte_carlo_probs,
        width,
        label="Monte Carlo",
        color="steelblue",
        alpha=0.8,
    )

    bars2 = ax.bar(
        [i + width / 2 for i in x],
        theoretical_probs,
        width,
        label="Theoretical",
        color="coral",
        alpha=0.8,
    )

    ax.set_xlabel("Sum of Dice", fontsize=12)
    ax.set_ylabel("Probability (%)", fontsize=12)
    title = "Monte Carlo Dice Simulation"
    if num_rolls:
        title += f" ({num_rolls:,} rolls)"
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    for bar in bars1:
        height = bar.get_height()
        if height > 0.5:
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"{height:.1f}%",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    for bar in bars2:
        height = bar.get_height()
        if height > 0.5:
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"{height:.1f}%",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    plt.tight_layout()
    plt.show()
