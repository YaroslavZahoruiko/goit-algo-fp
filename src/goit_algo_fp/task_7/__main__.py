from goit_algo_fp.task_7 import (
    monte_carlo_simulation,
    get_theoretical_probabilities,
    print_probability_table,
    plot_probabilities,
)


def main() -> None:
    print("=" * 70)
    print("Monte Carlo Simulation: Two Dice Rolls")
    print("=" * 70)

    num_rolls = 100000

    print("\nConfiguration:")
    print(f"  Number of rolls: {num_rolls:,}")
    print("\nRunning simulation...")

    probabilities = monte_carlo_simulation(num_rolls)

    theoretical = get_theoretical_probabilities()

    print_probability_table(probabilities, theoretical, num_rolls)
    plot_probabilities(probabilities, theoretical, num_rolls)

    print("\n" + "=" * 70)
    print("Summary Statistics")
    print("=" * 70)
    print(f"Most common sum: {max(probabilities, key=probabilities.get)}")
    print(f"Least common sum: {min(probabilities, key=probabilities.get)}")
    print(
        f"Expected sum (theoretical): {sum(s * p for s, p in theoretical.items()):.2f}"
    )
    print("=" * 70)


if __name__ == "__main__":
    main()
